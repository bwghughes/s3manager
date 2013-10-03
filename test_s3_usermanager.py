import unittest


class TestS3Manager(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass


if __name__ == '__main__':
    import os
    import sys
    loader = unittest.TestLoader()
    suite = loader.discover(os.curdir)
    unittest.TextTestRunner(sys.stdout, verbosity=1).run(suite)