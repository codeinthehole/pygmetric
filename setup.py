#!/usr/bin/env python
from setuptools import setup, find_packages

import pygmetric


setup(name='pygmetric',
      version=pygmetric.__version__,
      author="David Winterbottom",
      author_email="david.winterbottom@gmail.com",
      description="gmetric scripts written in python (for use with Ganglia)",
      long_description=open('README.rst').read(),
      packages=find_packages(),
      scripts=['bin/pygmetric_apache',
               'bin/pygmetric_nginx',
               'bin/pygmetric_rabbitmq',
               'bin/pygmetric_mysql',
              ])
