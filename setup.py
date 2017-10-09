#!/usr/bin/env python
#coding=utf-8

from setuptools import setup, find_packages


import sys
import re


if sys.version_info < (2, 6):
    sys.exit('Python 2.5 or greater is required.')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as fp:
    readme = fp.read()


setup(
    name = 'Doraemon',
    version = '0.1.0',
    keywords = ('Doraemon', 'mongodb','mongo','orm'),
    description = 'mongodb orm package ',

    long_description = readme,

    license = 'Apache Licence 2.0',

    url = 'https://github.com/x0fengluo/Doraemon',
    author = 'x0fengluo@gmail.com',
    author_email = 'x0fengluo@gmail.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)
