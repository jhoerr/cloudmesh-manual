Installation
============

Cloudmesh is easy to install. Dependent on your preferences you can choose an
install from

* pip if you are a cloudmesh user
* source install if you are a developer

At this time we do not recommend the conda install, as the conda packages are
outdated at this time.

Please read a section in this manual completly, and understand the items
explained. Do not just copy an past
text in your terminal and execute it as it could have unexpected consequences.

The mongo installation has to be done by everyone.

.. warning:: At this time we recommend that you do the source install as we
             have not yet uploaded all packages to pypi.

Prerequisites
-------------

.. note:: Before you install make sure that you have at minimum python 3.7.3
          installed. Likely the code will work with earlier versions, but we
          do the development in python 3.7.3 from https://www.python.org/downloads/.


Prerequisits Ubuntu 18.04
~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: We recommend you update your ubuntu version to 19.04 and
             follow the instructions for that version instead, as it is
             significantly easier. If you however are not able to do so, the
             following instructions may be helpful. 


We first need to make sure that the correct version of the Python3 is
installed. The default version of Python on Ubuntu 18.04 is 3.6. You can get
the version with::

    python3 --version

If the version is not 3.7.3 or newer, you can update it as follows:

.. code:: bash

    sudo apt-get update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install python3.7 python3-dev python3.7-dev

You can then check the installed version
using ``python3.7 --version`` which should be ``3.7.3``.

Now we will create a new virtual environment:

.. code:: bash

    python3.7 -m venv --without-pip ~/ENV3

The edit the ``~/.bashrc`` file and add the following line at the end:

.. code:: bash

    alias ENV3="source ~/ENV3/bin/activate"
    ENV3

now activate the virtual environment using:

.. code:: bash

    source ~/.bashrc

now you can install the pip for the virtual environment without conflicting
with the native pip:

.. code:: bash

    curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
    python get-pip.py
    rm get-pip.py

Prerequisits Ubuntu 19.04
~~~~~~~~~~~~~~~~~~~~~~~~~

Python 3.7 is installed in ubuntu 19.04. Therefore, it already fulfills the
prerequisits. However we recommend that you update to the newest version of
python and pip.


Prerequisits macOS
~~~~~~~~~~~~~~~~~~

Installing cloudmesh in macOS is very similar to installation in Ubuntu.
Start the process by installing the python 3 using ``homebrew``. Install the
``homebrew`` using the instruction in their `web page
<https://brew.sh/#install>`_:

.. code:: bash

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then you should be able to install Python 3.7.3 using:

.. code:: bash

    brew install python

Prerequisit venv
~~~~~~~~~~~~~~~~

.. _Use a venv:

This step is highly recommend if you have not yet already installed a
``venv`` for python to make sure you are not interfering with your system
python. This is simple. For our purposes we assume that you use the directory
 ~/ENV3. Follow these steps first:

.. code:: bash

   python3.7 -m venv  ~/ENV3
   source  ~/ENV3/bin/activate

You can add at the end of your .bashrc (ubuntu) or .bash_profile (macOS) file
the line

.. code:: bash

    source ~/ENV3/bin/activate

so the environment is always loaded. Now you are ready to install cloudmesh.

To make sure you have an up to date version of pip issue the command

.. code:: bash

    pip install pip -U

Installation with Pip
---------------------

.. warning:: At this time the pip install is not supported.

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
a configuration file. This is done by invoking the ``cms`` comamnd the first
time. Thus, just type the command


.. code:: bash

   cms help

in your terminal. It will create a directory ``~/.cloudmesh``
in which you can find the configuration file:

::

    ~/.cloudmesh/cloudmesh4.yaml


.. todo:: It would be beneficial to implement a command ``cms setup`` that
          does not only the yaml file, but also the mongo password.

Anaconda and Conda
------------------

.. warning:: At this time the conda install is not supported.

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

.. warning:: This is the only supported way to install cloudmesh at this time.

As a developer you want to use our source instalation. For this reasone we
wrote a ``cloudmesh-installer`` script that conveniently downloads the needed
repositories, installs and updates them on demand. More documentation about it
 can be found at

-  https://github.com/cloudmesh/cloudmesh-installer

First make sure you have a python ``venv`` as described in the pip section
(see `Use a venv`_). Now you can install it with

.. code:: bash

   pip install cloudmesh-installer

Next, it is best to create an empty directory and decide which bundles to
install

.. code:: bash

   mkdir cm
   cd cm
   cloudmesh-installer bundels

First, you have to decide which cloudmesh bundle to install. If you only want
to use compute resources the bundle name ``cloud`` will be what you want.
If in addition you also like to work on storage, the bundle name ``storage``
needs to be used.

Let, us assume you chose ``cloud``, than you can install cloudmesh with

.. code:: bash

   cloudmesh-installer git clone cloud
   cloudmesh-installer install cloud -e

It will take a while to install. On newer machines 1 minute, on older
significant longer. You can than test if you sucessfully installed it by
issueing the command

.. code:: bash

    cms help

You will see a list of commands. A directory ``~/.cloudmesh`` with some
default files will be installed, that you will need to modify at one point.


Updates
~~~~~~~

To update the source from github, simply use the command while making sure to
 specify the desired bundle name, let us assume you use ``cloud``

.. code:: bash

    cloudmesh-installer git pull cloud

Reinstalation
~~~~~~~~~~~~~

In case you need to reinstall cloudmesh and you have used previously the
cloudmesh-installer, you can do it as follows (We assume you have used venv
and the ``cloudmesh-installer`` in the directory cm as documented previously):

.. code:: bash

    cd cm # the directory wher eyour source locates
    cloudmesh-installer local purge . --force
    rm -rf ~/ENV3
    python3 -m venv ~/ENV3
    pip install pip -U
    pip install cloudmesh-installer
    cloudmesh-installer install cloud -e
    cms help

Please note that this will not work if you did not use the -e option previously.
Make sure to delete the old version, wherever you installed them.

.cloudmesh directory
--------------------

All cloudmesh related information is stored in the ``.cloudmesh`` directory.
In case you want to start fresh, simply delete that directory and its
subdirectories. However, if you need information form it make sure you make a
backup. Please note that in this file you have sensitive information and it
should never be backed up into github, box, icloud, or other such services.
Keep it on your computer or back it up on an secure encrypted external hard
drive or storage media only you have access to.


Installation of mongod
----------------------

First, you will need to install a ``cloudmesh4.yaml`` file, if you have not
done this before. The easieast way to do so is with the command

.. code:: bash

   cms help

Now you will need to edit the configuration file

.. code:: bash

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

However, please remember that for cloudmesh to work properly you need to start
mongo. In case you need a different port you can configure that in the yaml
file.




