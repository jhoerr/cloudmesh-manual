Cloudmesh Virtualbox/Vagrant Interface
======================================

Virtualbox provides a convenient way to manage virtual machines on a
local computer. Graphical user interfaces, a commandline client, but
also vagrant exist to access them. However we noticed that we often only
need a very small subset to start a vm and to tear it down. Remembering
the interfaces is difficult. Previously we developed a cloudmesh\_client
that has an easy to remember interface. We leverage from this experience
and introduce a very easy to remember commandline client. At the same
time we also allow a simpl python API to manage virtual machines on
virtualbox. We use vagrant internally. However vagrants focus on
directories and Vagrantfiles in a bit inconvenient also fo us, so we
provided wrappers and utelize the design of vagrant to our advantage
while only exposing the needed functionality.


# Vagrant

This has to be reimplemented for Python 3

```bash
cms set cloud=vagrant
```


For each named vbox a directory is created in whcih a Vagrant file is placed that than is used to interact with the virtual box
The location of teh directory is ~/.cloudmesh/vagrant/NAME.


If you set however the cloud to vbox you can save yourself the vbox command in consecutive calls and just use




```
Usage:
  cms version [--output=OUTPUT]
  cms image list [--output=OUTPUT]
  cms image find NAME
  cms image add NAME
  cms vm list [--output=OUTPUT] [-v]
  cms vm delete NAME
  cms vm config NAME
  cms vm ip NAME [--all]
  cms create NAME ([--memory=MEMORY]
                       [--image=IMAGE]
                       [--script=SCRIPT] | list)
  cms vm boot NAME ([--memory=MEMORY]
                        [--image=IMAGE]
                        [--port=PORT]
                        [--script=SCRIPT] | list)
  cms vm ssh NAME [-e COMMAND]
```


Examples
--------

### Listing vms

List the vms:

    cm-vbox vm list

  ------ --------- --------- ------------ ----------------------
  name   state     id        provider     directory

  w12 w1 running   47347b4   virtualbox   \~/w12 \~/w1
         running   db913dd   virtualbox   
  ------ --------- --------- ------------ ----------------------

### Listing images

List the images:

    cm-vbox image list

  ----------------- ------------ --------------
  name              provider     date

  ubuntu/trusty64   virtualbox   20160406.0.0
  ----------------- ------------ --------------

### Booting vms

Start a vm while taking an ubuntu image as default:

    cm-vbox vm boot w12

### Login

To login into a vm you can use the ssh command followed by the VM:

    cm-vbox vm ssh w12

where w12 is the name of the vm.

### Executing a command

To just execute a command, use:

    cm-vbox vm ssh w12 -e uname

### Destroy a vm

Deletes the specified vm:

    cm-vbox vm delete w12

### Create a Vagrantfile

Creates a Vagrantfile in ./w12/Vagrantfile:

    cm-vbox create w12

### Destroy the directory of the vm

Assume you like to destroy also the directory with all information about
the previously run vm you can simple delete it with rm:

    cm-vbox vm delete w12
    rm -r w12

Please not that wen you delet the directory the list command will
automatically remove it from the available vms. Hoewver before you
delete it is advisable to destroy the vm so you do not have the vm any
longer running.
