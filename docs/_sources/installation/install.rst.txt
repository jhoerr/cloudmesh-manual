Installation
============

Cloudmesh is easy to install. Dependent on your preferences you can choose an install from

* pip if you are a cloudmesh user
* source install if you are a developer

At this time we do not recommend the conda install, as the conda packages are outdated at this time.

Please read a section in this manual completly, and understand the items explained. Do not just copy an past
text in your terminal and execute it as it could have unexpected consequences.

The mongo installation has to be done by everyone.

.. warning:: At this time we recommend that you do the source install as we have not yet uploaded all packages to pypi.

Prerequisites
-------------


.. note:: Before you install make sure that you have at minimum python 3.7.3
          installed. Likely the code will work with earlier versions, but we
          do the development in python 3.7.3 from https://www.python.org/downloads/.

.. _Use a venv:


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

.. warning:: At this time we recommend that you do the source install as we have not yet uploaded all packages to pypi.

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

Anaconda and Conda
------------------

.. warning:: At this time we recommend that you do the source install as we have not yet uploaded all packages to
condahub.

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


Installation with cloudmesh-installer
-------------------------------------
This is by far the most convenient way of installing and managing the cloudmesh bundles and packages.


cloudmesh-installer in Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


18.04
^^^^^

To install ``cloudmesh-installer`` in Linux, we first need to make sure that
the correct version of the Python3 is
installed (version 3.7.3).

.. code:: bash

    sudo apt-get update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install python3.7 python3-dev python3.7-dev

The default version of Python on Ubuntu 18.04 is 3.6 and you can get that
version using ``python3 --version``. You can then check the installed version
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

now you should be able to install ``cloudmesh-installer``:

.. code:: bash

    pip install cloudmesh-installer

You should be able to now get the help function of the ``cloudmesh-installer``:

.. code:: bash

    cloudmesh-installer --help

You can now get the list of available bundles and install the bundle of your
choice. You can get the list of available bundles using:

.. code:: bash

    cloudmesh-installer bundles

Now, go to your target destination, e.g. ``~/cm`` and run the following
command to clone the ``cms`` bundle:

.. code:: bash

    cloudmesh-installer git clone cms

Now that the ``cms`` is cloned, you can then install the ``cms`` using the
following command:

.. code:: bash

    cloudmesh-installer install cms -e

Test the ``cms`` installation using:

.. code:: bash

    cms help


19.04
^^^^^

Ubuntu 19.04 has python 3.7 by default. There is no need to update python, just
use venv as discussed in the prerequisits.


cloudmesh-installer in macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing cloudmesh in macOS is very similar to installation in Ubuntu.
Start the process by installing the python 3 using ``homebrew``. Install the
``homebrew`` using the instruction in their `web page
<https://brew.sh/#install>`_:

.. code:: bash

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then you should be able to install Python 3.7.3 using:

.. code:: bash

    brew install python

The rest of the installation is identical to ubuntu. Start with creating the
virtual environment without pip, install pip separately, install
``cloudmesh-installer``, followed by cloning bundles and installing them.


Reinstalation
~~~~~~~~~~~~~

In case you need to reinstall cloudmesh and you have used previously the
cloudmesh-installer, you can do it as follows (We assume you have used the
cloudmesh-installer in the directory cm):

.. code:: bash

    cd cm # the directory wher eyour source locates
    cloudmesh-installer local purge . --force
    rm -rf ~/ENV3
    python3 -m venv ~/ENV3
    pip install pip -U
    pip install cloudmesh-installer
    cloudmesh-installer install cms -e
    cloudmesh-installer install cloud -e

Please note that this will not work if you did not use the -e option previously.
Make sure to delete the old version, wherever you installed it.

Installation of mongod
----------------------

First, you will need to install a ``cloudmesh4.yaml`` file, if you have not
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



