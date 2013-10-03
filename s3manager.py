import os
import logging

import boto
from boto.exception import BotoServerError

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

S3_ACCESS_ID = os.environ.get('S3_ACCESS_ID')
S3_SECRET = os.environ.get('S3_ACCESS_SECRET')
USER_GROUP = 'customers'

def get_iam_connection():
    try:
        iam_connection = boto.connect_iam(S3_ACCESS_ID, S3_SECRET)
        return iam_connection
    except BotoServerError:
        log.fatal("Failed to connect to IAM service.")


def create_bucket(iam_connection=None):
    pass


def add_user_to_group(iam_connection=None, username=None):
    try:
        iam_connection.add_user_to_group(USER_GROUP, username)
    except BotoServerError:
        log.fatal("Failed to add user to group.")


def create_user(iam_connection=None, username=None):
    try:
        response = iam_connection.create_user(username)
        response = iam_connection.  (username)
        access_key, secret_key = response.access_key.get('access_key_id'),\
                                 response.access_key.get('secret_access_key')
        return username, access_key, secret_key
    except BotoServerError:
        log.fatal("Failed to create user.")
