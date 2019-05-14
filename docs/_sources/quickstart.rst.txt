Quickstart
==========

One of the features up Cloudmesh is to easily start new virtual machines
on vairous clouds. It uses defaults for these clouds that can be chaned,
but are easily stored in a yaml file located at
``~/.cloudmesh/cloudmesh4.yaml`` This file is created upon first start
of the shell. You need to edit it and include some of your cloud
information.

A template for the yaml file is located at:

-  https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/etc/cloudmesh4.yaml


Manual
------

Before we start it is important to note that cloudmesh provides a quick lin
to its documentation. you can reach it with

.. code:: bash

   cms open doc

In case you are a developer and have installed the manual locally, you can
also obtain it with

.. code:: bash

   cms open doc local


Command line
------------

It is easy to switch beteeen clouds with the set command. Ater the set
and specifying the cloud by name many commands will default to that
cloud. The exception is the ``vm list`` command that lists by default
all vms on all clouds. In addition the ``vm refresh`` command will also
work on all clouds.

.. code:: bash

   cms admin mongo create  # needs only be done one time
   cms admin mongo start

   cms set cloud=vagrant
   cms vm start
   cms image list
   cms flavor list

   cms set cloud=aws
   cms vm start
   cms image list
   cms flavor list

   cms set cloud=azure
   cms vm start
   cms image list
   cms flavor list

   cms set cloud=chameleon
   cms vm start
   cms image list
   cms flavor list

   cms set cloud=jetstream
   cms vm start
   cms image list
   cms flavor list

   cms vm refresh

   cms vm list

   cms admin mongo stop

In case you want a command explicitly apply to one or more clouds or one
or more vms, they can be specified by name such as

.. code:: bash

   cms vm list --name vm[0-100]
   cms vm list --cloud aws,azure

Defaults for the cloud and the name can be specified through set such as

.. code:: bash

   cms set name=vm[0-100]
   cms set cloud=aws,azure


.. todo:: check if multiple clouds can be set and the list command works on
          multiple clouds. Check this also for image and flavor commands

Using the commands

.. code:: bash

   cms vm list

would than add the appropriate options to the command. To reset the show
to all vms set name and cloud to all

.. code:: bash

   cms set name=all
   cms set cloud=all

Interactive shell (proposed)
----------------------------

Cloudmesh uses cmd5 for its shell implementation and thus all commands
that are typed in in the terminal can also be typed in into a shell that
is started with cms

.. code:: bash

   cms
   cms> set cloud=aws
   cms> vm start

Command scripts
---------------

As we use cmd5 we also have access to piped and named scripts with

.. code:: bash

   echo script.cms | cms

and

.. code:: bash

   cms --script script.cms

Cache
-----

All information about for example virtual machines are cached locally.
The cache for various information sources can be explicitly updated with
the ``--refresh`` flag. Thus the command

.. todo:: check if the list --refresh is implemented for vm, flavor, imgages,
          for all clouds

.. code:: bash

   cms vm list --refresh
   cma flavor list --refresh
   cma image list --refresh

would first execute a refresh while the command

.. code:: bash

   cms vm list
   cms flavor list
   cms image list

would only read from the local cache

To change the behavior and always do a refresh you can use the command

.. code:: bash

   cms set refresh=True

To switch it off you can say

.. code:: bash

   cms set refresh=False

.. todo:: check if refresh=True this is implemented.
