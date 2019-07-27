Installation
============

Cloudmesh is easy to install. Dependent on your preferences you can choose an
install from

* pip if you are a cloudmesh user
* source install if you are a developer

Please read the instalatio section in this manual completely, and understand
the items explained before you install. Do not just paste and copy text in
your terminal and execute it as it could have unexpected consequences.

.. warning:: At this time we do not recommend the conda install, as the conda
             packages are outdated.

Prerequisites
-------------

.. note:: Before you install make sure that you have at minimum python 3.7.4
          installed. Likely the code will work with earlier versions, but we
          do the development in python 3.7.4. This version can be downloaded
          and installed from https://www.python.org/downloads/.

Prerequisits Ubuntu 19.04
^^^^^^^^^^^^^^^^^^^^^^^^^

Python 3.7 is installed in ubuntu 19.04. Therefore, it already fulfills the
prerequisits. However we recommend that you update to the newest version of
python and pip. However we recommend that you update the the newest version
of python. Please visit: https://www.python.org/downloads/


Prerequisits macOS
^^^^^^^^^^^^^^^^^^

Installation from Apple App Store
"""""""""""""""""""""""""""""""""

You want a number of useful tool on your macOS. They are not installed by
default, but are available via Xcode. First you need to install xcode from

* https://apps.apple.com/us/app/xcode/id497799835

Next you need to install macOS xcode command line tools::

    xcode-select --install

Installation from python.org
""""""""""""""""""""""""""""

The easiest instalation of Python for cloudmesh is to use the instaltion from
https://www.python.org/downloads. Please, visit the page and follow the
instructions. After this install you have `python3` avalable from the
commandline

Installation from Hoembrew
""""""""""""""""""""""""""

An alternative instalation is provided from Homebrew. To use this install
method, you need to install Homebrew first. Start the process by installing
the python 3 using ``homebrew``. Install ``homebrew`` using the
instruction in their `web page <https://brew.sh/#install>`_:

.. code:: bash

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then you should be able to install Python 3.7.4 using:

.. code:: bash

    brew install python


Prerequisits Ubuntu 18.04
^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning:: We recommend you update your ubuntu version to 19.04 and
             follow the instructions for that version instead, as it is
             significantly easier. If you however are not able to do so, the
             following instructions may be helpful.


We first need to make sure that the correct version of the Python3 is
installed. The default version of Python on Ubuntu 18.04 is 3.6. You can get
the version with::

    python3 --version

If the version is not 3.7.4 or newer, you can update it as follows:

.. code:: bash

    sudo apt-get update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install python3.7 python3-dev python3.7-dev

You can then check the installed version
using ``python3.7 --version`` which should be ``3.7.4``.

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


Prerequisits Windows 10
^^^^^^^^^^^^^^^^^^^^^^^

On Windows 10 you can install cloudmesh in either the system or a Linux
Subsystem. We recommend that you use the Professional or the Educational
version of Windows as the Home eddition is very limitted. Alternatively, you
can also use the docker version of cloudmesh.

.. warning:: The docker version of cloudmesh is still under development.

.. warning:: We do not recommend or suppport other versions of Windows.

System Install
""""""""""""""

Python 3.7 can be installed on Windows 10 using: https://www.python.org/downloads/

Linux Subsystem Install
"""""""""""""""""""""""

To activate the Linux Subsystem, please follow the instructions at

* https://docs.microsoft.com/en-us/windows/wsl/install-win10

A suitable distribution would be

* https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab

However as it uses an older version of python you will ahve to update it.

Prerequisit venv
^^^^^^^^^^^^^^^^

.. _Use a venv:

This step is highly recommend if you have not yet already installed a
``venv`` for python to make sure you are not interfering with your system
python. Not using a venv could have catastrophic consequences and a
destruction of your operating system tools if they realy on Python. The use
of venv is simple. For our purposes we assume that you use the directory::

    ~/ENV3

Follow these steps first:

.. code:: bash

   python3 -m venv  ~/ENV3
   source ~/ENV3/bin/activate

You can add at the end of your .bashrc (ubuntu) or .bash_profile (macOS) file
the line

.. code:: bash

   source ~/ENV3/bin/activate

so the environment is always loaded. Now you are ready to install cloudmesh.

Check if you have the right version of python installed with

.. code:: bash

   python --version

To make sure you have an up to date version of pip issue the command

.. code:: bash

   pip install pip -U

Installation with Pip
---------------------

If you like to use cloudmesh as user, the installation can be done with pip.
Cloudmesh is stritributes in different modules and you only need to install
the modules you desire. Dependent on your needs
you can install the cloudmesh `cloud` or `storage` bundle with:

.. code:: bash

   pip install cloudmesh-cloud

or

.. code:: bash

   pip install cloudmesh-storage # not yest supported

Please note that the storage bundle also includes `cloudmesh-cloud`
.Additional packages include but are not yet released:

.. code:: bash

   pip install cloudmesh-flow    # not yet supported
   pip install cloudmesh-emr     # not yet supported
   pip install cloudmesh-batch   # not yet supported
   pip install cloudmesh-openapi # not yet supported


You want to test the cloudmesh command and at the same time create
a configuration file. This is done by invoking the ``cms`` command the first
time. Thus, just type the command


.. code:: bash

   cms help

in your terminal. It will create a directory ``~/.cloudmesh``
in which you can find the configuration file:

::

    ~/.cloudmesh/cloudmesh4.yaml


Anaconda and Conda
------------------

.. warning:: At this time the conda install is not supported.

We also have the base packages available as conda packages on conda hub
in the chanel ``laszewski``. This includes

-  cloudmesh-common
-  cloudmesh-cmd5
-  cloudmesh-sys

Note that the conda packages will always be a behind the version you will
find in pypi. Therefore we recommend you use the pip based installation.


Source Installation for Developers
----------------------------------

As a developer you want to use our source installation. For this reason we
wrote the ``cloudmesh-installer`` script that conveniently downloads the
needed repositories, installs and updates them on demand. More documentation
about it can be found at

-  https://github.com/cloudmesh/cloudmesh-installer

First make sure you have a python ``venv`` as described in the pip section
(see `Use a venv`_). Now you can install it with

.. code:: bash

   pip install cloudmesh-installer

Next, it is best to create an empty directory and decide which bundles to
install while listing them

.. code:: bash

   mkdir cm
   cd cm
   cloudmesh-installer bundels

Once you have decided whihc bundle to install you can proceed. If you only want
to use compute resources the bundle name ``cloud`` will be what you want.
If in addition you also like to work on storage, the bundle name ``storage``
needs to be used.

Let, us assume you chose ``cloud``, than you can install cloudmesh with

.. code:: bash

   cloudmesh-installer git clone cloud
   cloudmesh-installer install cloud -e

The `-e` option is very important as it compiles the code in place of the
downloaded directories and in case of changes in the directory automatically
makes them available to the instaled version. This is naturally very
important. It will take a while to install. On newer machines 1 minute, on older
significant longer. Please watch your system information if the install
takes a long time. Afterthe instalation is complete, you can than test if you
successfully installed it by issuing the command

.. code:: bash

    cms help

You will see a list of commands. A directory ``~/.cloudmesh`` with some
default files will be installed, that you will need to modify at one point.


Updates
^^^^^^^

To update the source from github, simply use the `cloudmesh-installer` command
while making sure to specify the desired bundle name, let us assume you use
``cloud``

.. code:: bash

    cloudmesh-installer git pull cloud

If you see any conflicts make sure to resolve them. As developer sometimes it
may be best to make a backup of the `cm` directory aor individual
repositories in the cm directory. Then copy your changes
into the newest code. Make sure to remove all python artifacts created with
the -e option. See the command

.. code:: bash

    cd cm
    cloudmesh-installer local purge .


Reinstallation
^^^^^^^^^^^^^^

In case you need to reinstall cloudmesh and you have used previously the
cloudmesh-installer, you can do it as follows (We assume you have used venv
and the ``cloudmesh-installer`` in the directory cm as documented previously):

.. code:: bash

    cd cm # the directory where your source locates
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
done this before. If you do have mongo, you can safe this step. However,
make sure you do not expose mongo on the internet so that you keep your
information in mongo private. The easiest way to install mongo is with our
build in install script. You will need to set first permission to use this
install.  To do so start with the command

.. code:: bash

   cms help

Now you will need to edit the configuration file

.. code:: bash

    emacs ~/.cloudmesh/cloudmesh4.yaml

and change the password of the mongo entry to something you like, e.g. change
the TBD to a real strong password::

   MONGO_PASSWORD: TBD

In case you do not have mongod installed, you can do so for macOS and Ubuntu
18.xx by setting the following variable::

   MONGO_AUTOINSTALL: True

Now you can run the ``admin mongo install`` command. It will not only install
mongo, but also add the path to your ``.bash_*`` file. In case
of windows platform, you will have to set the PATH variable manually. To
install it simply say.

Alternatively you can set thes values form the commandline without using an
editor with

.. code:: bash

    cms config set cloudmesh.data.mongo.MONGO_AUTOINSTALL=True
    cms config set cloudmesh.data.mongo.MONGO_PASSWORD=YOURPASSWORD

Make sure to set a good strong password for Mongo that you can remember

Now you can install mongo conveniently from cloudmesh if you have not
installed it. On macOS and ubuntu it will install it under::

    ~/local/mongo/bin.

Please make sure that this path is added to your PATH variable after the
install is complete.

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

Please remember that for cloudmesh to work properly you need to start
mongo. In case you need a different port you can configure that in the yaml
file.

Prerequisit ssh key
^^^^^^^^^^^^^^^^^^^

In order for you to use cloudmesh you will need an ssh key. This can be
created from the command line with

.. code:: bash

    ssh-keygen

Please make sure to use a passphrase with your key. Anyone telling you to use
a passwordless key is giving you a wrong advice.



