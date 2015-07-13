#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

setup(
    name='awscli-keyring',
    version='0.1.2',
    description='AWS command line credentials from OS X Keychain and other keyrings.',
    long_description='AWS command line credentials from OS X Keychain and other keyrings.',
    author='Samuel Cochran',
    author_email='sj26@sj26.com',
    url='https://github.com/sj26/awscli-keyring',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'awscli',
        'keyring',
    ],
    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
