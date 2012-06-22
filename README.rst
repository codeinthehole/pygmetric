=========
pygmetric
=========

A collection of gmetric scripts written in Python.

Install
-------
Ensure server has packages required to install::

    apt-get install python-pip git-core

then::

    pip install -e git+git://github.com/codeinthehole/pygmetric.git#egg=pygmetric

Finally, create a cronfile ``/etc/cron.d/ganglia-node`` with contents::

    * * * * * root /usr/local/bin/pygmetric_apache


