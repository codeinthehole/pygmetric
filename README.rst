=========
pygmetric
=========

A collection of gmetric scripts written in Python.  Included at the moment are:

* Apache
* Nginx
* Rabbitmq
* MySQL

Install
-------

Ensure your server has the required packages::

    sudo apt-get install python-setuptools git-core

Now upgrade pip itself::

    sudo easy_install pip

which can lead to an alternative pip executable to the system one.  For the
below commands, ensure you are using the latest pip version.

Install pygmetric from Github::

    sudo pip install git+git://github.com/codeinthehole/pygmetric.git#egg=pygmetric

Finally, create a cronfile ``/etc/cron.d/ganglia-node`` which calls the
appropriate metric executables.  An example would be::

    MAILTO=your.email@address

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

MySQL
~~~~~

You need to set up a user for pygmetric to connect as.  Ensure this user only
has read access.

For pygmetric to fetch stats, the following command needs to work::

    mysqladmin extended --user=$USERNAME --password=$PASSWORD

Nginx
~~~~~

You need to ensure that Nginx stats are available on ``/nginx_status``.

Usage
-----

Each command's options can be found be running the ``pygmetric_*`` executable
with the ``--help`` option.

