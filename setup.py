#!/usr/bin/env python

"""
S3UserManager
-------------

Elegant user and bucket manager for S3.
"""
from setuptools import setup


setup(
    name='S3UserManager',
    version='0.1',
    url='https://github.com/bwghughes/s3usermanager',
    license='See License',
    author='Ben Hughes',
    author_email='bwghughes@gmail.com',
    description='Elegant user and bucket manager for S3.',
    long_description=__doc__,
    py_modules=['s3_usermanager'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'boto',
        'wsgiref'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)