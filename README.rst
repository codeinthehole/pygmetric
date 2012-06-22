=========
pygmetric
=========

A collection of gmetric scripts written in Python.  Included at the moment are:

* Apache

Install
-------

Ensure server has packages required to install::

    apt-get install python-pip git-core

Now upgrade pip itself::

    pip install -U pip

which can lead to an alternative executable to the system one.

Then::

    pip-2.6 install -e git+git://github.com/codeinthehole/pygmetric.git#egg=pygmetric

Finally, create a cronfile ``/etc/cron.d/ganglia-node`` with contents::

    * * * * * root /usr/local/bin/pygmetric_apache

Prerequisites
-------------

Apache
~~~~~~

You need to ensure that Apache statistics are fetched on ``/server-status?auto``
of the host you are monitoring.  Test this using the ``www-browser`` command::

    www-browser -dump http://localhost/server-status?auto

You should see something like::

    Total Accesses: 5998780
    Total kBytes: 27975841
    CPULoad: .00905916
    Uptime: 4246639
    ReqPerSec: 1.41259
    BytesPerSec: 6745.87
    BytesPerReq: 4775.51
    BusyWorkers: 1
    IdleWorkers: 9
    Scoreboard:
    W__.______._........................................................
    ................................................................................
    ................................................................................
    ............................

Usage
-----

Each command's options can be found be running the ``pygmetric_*`` executable
with the ``--help`` option.

