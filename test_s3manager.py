import uuid
import unittest
from mock import patch, Mock
from nose.plugins.attrib import attr

import boto
from s3manager import get_iam_connection, add_user_to_group, USER_GROUP,\
                      create_user
from boto.exception import BotoServerError

class UnitTestS3Manager(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_iam_connection(self):
        with patch('boto.connect_iam') as connect:
            get_iam_connection()
            assert connect.called_once

    def test_get_iam_connection_logs_error_when_fails(self):
        with patch.object(boto, 'connect_iam') as connect:
            with patch('s3manager.log') as log:
                connect.side_effect = BotoServerError(Mock(), Mock())
                get_iam_connection()
                self.assertRaises(BotoServerError)
                assert log.fatal.called

    def test_add_user_to_group(self):
        mock_iam = Mock()
        mock_username = Mock()
        add_user_to_group(iam_connection=mock_iam, username=mock_username)
        mock_iam.add_user_to_group.assert_called_with(USER_GROUP, mock_username)

    def test_add_user_to_group_fails_gracefully(self):
        mock_iam = Mock()
        mock_iam.side_effect = BotoServerError(Mock(), Mock())
        mock_username = Mock()
        add_user_to_group(iam_connection=mock_iam, username=mock_username)
        mock_iam.add_user_to_group.assert_called_with(USER_GROUP, mock_username)
        self.assertRaises(BotoServerError)

    def test_create_user(self):
        mock_iam = Mock()
        mock_username = Mock()
        username, access_key, access_secret = create_user(iam_connection=mock_iam,
                                                          username=mock_username)
        mock_iam.create_user.assert_called_with(mock_username)
        mock_iam.create_access_key.assert_called_with(mock_username)
        assert username == mock_username
        assert isinstance(access_key, Mock)
        assert isinstance(access_secret, Mock)

    def test_create_user_fails_gracefully(self):
        mock_iam = Mock()
        mock_iam.side_effect = BotoServerError(Mock(), Mock())
        mock_username = Mock()
        username, access_key, access_secret = create_user(iam_connection=mock_iam,
                                                          username=mock_username)
        self.assertRaises(BotoServerError)

@attr('integration')
class FunctionalTestS3Manager(unittest.TestCase):
    def setUp(self):
        self.conn = get_iam_connection()
        self.username = 'test-username-{}'.format(uuid.uuid4())

    def test_get_iam_connection(self):
        groups = self.conn.get_all_groups()
        assert groups

    def test_create_user(self):
        username, access_key, access_secret = \
                    create_user(iam_connection=self.conn, username=self.username)
        self.access_key, self.access_secret = access_key, access_secret
        assert access_key
        assert access_secret
        self.conn.remove_user_from_group(USER_GROUP, self.username)
        self.conn.delete_access_key(access_key, self.username)
        self.conn.delete_user(self.username)


    def tearDown(self):
        self.conn = None


if __name__ == '__main__':
    import os
    import sys
    loader = unittest.TestLoader()
    suite = loader.discover(os.curdir)
    unittest.TextTestRunner(sys.stdout, verbosity=1).run(suite)