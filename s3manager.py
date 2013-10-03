import os
import uuid
import logging
import argparse

import boto
from boto.exception import BotoServerError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

USER_GROUP = 'application-users'

def get_iam_connection():
    try:
        iam_connection = boto.connect_iam()
        return iam_connection
    except BotoServerError:
        log.fatal("Failed to connect to IAM service.")


def create_bucket(iam_connection=None, username=None):
    pass


def add_user_to_group(iam_connection=None, username=None):
    try:
        groups = iam_connection.get_all_groups()
        iam_connection.add_user_to_group(USER_GROUP, username)
    except BotoServerError:
        log.fatal("Failed to add user to group.")


def create_user(iam_connection=None, username=None):
    try:
        log.info('Creating {} user and adding to {} group'.format(username,
                                                                  USER_GROUP))
        response = iam_connection.create_user(username)
        add_user_to_group(iam_connection, username)
        response = iam_connection.create_access_key(username)
        access_key, secret_key = response.access_key.get('access_key_id'),\
                                 response.access_key.get('secret_access_key')
        return username, access_key, secret_key
    except BotoServerError:
        log.fatal("Failed to create user.")

def send_email(email_address):
    pass


def main():
    parser = argparse.ArgumentParser(description='IFA Secure Command Line Application')
    parser.add_argument('--name', action="store", dest="name")
    parser.add_argument('--email', action="store", dest="email")
    parser.add_argument('--password', action="store", dest="password")
    parser.add_argument('--bucket', action="store_true", dest="bucket", default=True)
    parser.add_argument('--send-email', action="store_true", dest="send_email", default=True)
    options = parser.parse_args()
    connection = get_iam_connection()
    create_user(iam_connection=connection ,username="test-user-{}".format(uuid.uuid4()))