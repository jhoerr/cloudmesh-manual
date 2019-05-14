Installation
============

Prerequisites
-------------


.. note:: Before you install make sure that you have at minimum python 3.7.3
          installed. Likely the code will work with earlier versions, but we
          do the development in python 3.7.3.

.. _Use a venv:

Use a venv
~~~~~~~~~~

We highly recommend that you use a python virtualenv such as ``venv`` to
make sure you are not interfering with your system python. This is
simple. For our purposes we assume that you use the directory ~/ENV3.
Follow these steps first:

.. code:: bash

   python3.7 -m venv  ~/ENV3
   source  ~/ENV3/bin/activate

You can add at the end of your .bashrc or .bash_profile file the line

.. code:: bash

    source ~/ENV3/bin/activate

so the environment is always loaded. Now you are ready to install cloudmesh.

Installation with Pip
---------------------

The instalation can be done with pip.

.. code:: bash

   pip install cloudmesh-cms
   pip install cloudmesh-sys
   pip install cloudmesh-cloud
   pip install cloudmesh-storage

Additional packages include but are not yet released:

.. code:: bash

   pip install cloudmesh-flow
   pip install cloudmesh-emr
   pip install cloudmesh-batch
   pip install cloudmesh-openapi


Next you will need to test the cloudmesh command and at the same time create
a configuration file. This is done by invoking the `cms` comamnd the first time.
Thus, just type the command


.. code:: bash

   cms help

in your terminal. It will create a directory ``~/.cloudmesh``
in which you can find the configuration file:

::

    ~/.cloudmesh/cloudmesh4.yaml


.. todo:: check if this realy works, it woudl be beneficial to implement a
          command ``cms setup`` that does not only the yaml file, but also the
          mongo password

Installation of mongod
----------------------

First, you will need to install a ``cloudmesh4.yaml``file, if you have not
done this before. The easieast way to do so is with the command

.. code:: bash

   cms help

Now you will need to edit the configuration file

::

    emacs ~/.cloudmesh/cloudmesh4.yaml

and change the password of the mongo entry to something you like, e.g. change
the TBD to a real strong password

::

   MONGO_PASSWORD: TBD

In case you do not have mongod installed, you can do so for macOS and Ubuntu
18.xx by setting the following variable:

::

   MONGO_AUTOINSTALL: True

Now you can run the ``admin mongo install`` command. It will not only install
mongo, but also add the path to your ``.bash_*`` file. In case
of windows platform, you will have to set the PATH variable manually. To
install it simply say.

.. code:: bash

   cms admin mongo install

As we password protect mongo, you will need to first run the command

.. code:: bash

    cms admin mongo create

Now you can start mongo for cloudmesh with

.. code:: bash

   cms admin mongo start

In case you need to stop it you can use the command

.. code:: bash

   cms admin mongo stop

However, please remember that for cloudmesh to work properly, please start
mongo. In case you need a different port you can configure that in the yaml
file.


Anaconda and Conda
------------------

We also have the base packages available as conda packages on conda hub
in the chanel ``laszewski``. This includes

-  cloudmesh-common
-  cloudmesh-cmd5
-  cloudmesh-sys

Note that the packages will always be a behind the packages on pypi and
especially the source distribution. FUrthermore, other packages are not yet
uploaded. If you are interested in helping out with the conda packages, let
us know. Please contact us if you need a new release. As conda supports alos
pip, we recommend using pip for it also.



Source Installation for Developers
----------------------------------

As a developer you want o use our source instalation. For this reasone we
wrote a cloudmesh-installer script that conveniently downloads the needed
repositories. More documentation about it can be found at

-  https://github.com/cloudmesh/cloudmesh-installer

First make sure you have a python virtual env as described in the pip section
(see `Use a venv`_). Instead of using the pip install method, please use the
following.

Now you can install it with

.. code:: bash

   pip install cloudmesh-installer

It is best to create an empty directory and decide which bundles to
install

.. code:: bash

   mkdir cm
   cd cm
   cloudmesh-installer bundels

Decide which bundels you like to install (let us assume you use storage)
and simply say

.. code:: bash

   cloudmesh-installer git clone storage
   cloudmesh-installer install storage -e

It will take a while to install On newer machines 1 minte, on older
significant longer. You can than test if


