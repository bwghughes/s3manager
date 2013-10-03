S3 Manager
======

An elegant API to manage users and buckets in S3, built on top of the
legendary [boto](https://github.com/boto/boto)

Note: You will need to set up some master AWS Credentials to do this.
For more informations see [here](http://docs.pythonboto.org/en/latest/s3_tut.html)

Quick Start
------

To create a user with access to a single bucket try the following:

```
import uuid
from s3_manager import create_user_and_bucket

def main():
    user_name = "someuserdudeguychap@flipper.com"
    aws_access_id, aws_access_secret = create_user_and_bucket(user_name)

if __name__ == '__main__':
    main()

```