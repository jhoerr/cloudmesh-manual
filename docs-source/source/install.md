# Installation

## Prerequisites

Before you install make sure that you have at minimum python 3.7.3
installed. Likely the code will work with earlier versions, but we do 
the development in python 3.7.3.


We recommend that you use a python virtualenv such as `venv` to make sure 
you are not interfering with your system python. This is simple. For our purposes 
we assume that you use the directory ~/ENV3. Follow these steps first:


```bash
$ python3 -m venv  ~/ENV3
$ source  ~/ENV3/bin/activate
```

You can add at the end of your .bashrc or .bash_profile file the line

```
source ~/ENV3/bin/activate
```

so the environment is always loaded. Now you are ready to install cloudmesh.

### Installation via pip development


The instalation can be done with pip. 

```bash
$ pip install cloudmesh-cms
$ pip install cloudmesh-sys
$ pip install cloudmesh-cloud
$ pip install cloudmesh-storage
```

Additional packages include but are not yet released:

```
$ pip install cloudmesh-flow
$ pip install cloudmesh-emr
$ pip install cloudmesh-batch
$ pip install cloudmesh-openapi
```



### Source installation for development

As a developer you want o use our source instalation. For this reasone we wrote a cloudmesh-installer script that 
conveniently downloads the needed repositories. More documentation about it can be found at 

* <https://github.com/cloudmesh/cloudmesh-installer>

You install it with 

```bash
$ pip install cloudmesh-installer
```

It is best to create an empty directory and decide which bundles to install

```bash
$ mkdir cm
$ cd cm
$ cloudmesh-installer bundels
```

Decide which bundels you like to install (let us assume you use storage) and
simply say

```bash
$ cloudmesh-installer git clone storage
$ cloudmesh-installer install storage -e
```

It will take a while to install On newer machines 1 minte, on older significant
longer. You can than test if 

``` bash
$ cms help 
```

works. Make susre to stay up to date while issuing the pull command on your
bundle

```bash
$ cloudmesh-installer git pull bundle
$ cloudmesh-installer install storage -e

```


## Installation of mongod

First, you will need to install a `cloudmesh4.yaml` file, if you have
not done this before. The easieast way to do so is with the command

```bash
$ cms help
```
 
Now you will need to edit the file

`~/.cloudmesh/cloudmesh4.yaml`

and change the password of the mongo entry to something you like,
 e.g. change the TBD to a real strong password

```
MONGO_PASSWORD: TBD
```

In case you do not have mongod installed, you can do so for macOS and Ubuntu 
18.xx by setting the following variable:

```
MONGO_AUTOINSTALL: True
```


Now you can run the `admin mongo install` command. It will not only
install mongo, but also add the path to your `.bash_*` file. In case
of windows platform, you will have to set the PATH variable
manually. To install it simply say.

```bash
$ cms admin mongo install
```

To create a password protection you than run the command

```bash $ cms admin mongo create ``` In case of Windows platform, after
executing above command, open a new cms session and execute below
commands.

```bash
$ cms admin mongo start
```

Once the mongo db is created it can be started and stoped with 

```bash
$ cms admin mongo start
$ cms admin mongo stop
```

For cloudmesh to work properly, please start mongo.


## Anaconda and Conda

We also have the base packages available as conda packages on conda hub in the
chanel `laszewski`. This includes

* cloudmesh-common
* cloudmesh-cmd5
* cloudmesh-sys

Note that the packages will always be a little bit behind the packages on pypi
and especially the source distribution. If you are interested in helping out
with the conda packages, let us know.
