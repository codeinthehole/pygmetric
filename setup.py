#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='pygmetric',
      version='0.1',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="gmetric scripts written in python (for used with Ganglia)",
      long_description=open('README.rst').read(),
      packages=find_packages(),
      scripts=['bin/pygmetric_apache',
               'bin/pygmetric_nginx',
               'bin/pygmetric_rabbitmq',
               'bin/pygmetric_mysql',
              ])
