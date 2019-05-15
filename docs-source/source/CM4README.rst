CM4 Details (outdated)
======================

In cloudmesh, we are using the **Python** tool to implement a program
that could remotely control cloud nodes provided by different
organizations and run experiments in parallel.

The goal of *``cloudmesh``* is to provide a platform that users could
directly control the nodes they have, like AWS, Azure, and OPENSTACK
instances. Users could decide to start, stop, destroy, create, resume,
and suspend different nodes without accessing the **Console** interfaces
of providers. Then users could install experiment environment, software,
and other required tools in these running nodes. Finally, an experiment
could be executed in running nodes by sending the commands from
*``cloudmesh``* platform. Meanwhile, we embed the NoSQL database
**MongoDB** into cloudmesh for managing the nodes and experiments.

Getting the config object
-------------------------

.. code:: python

   from cloudmesh.cloud.configuration.config import Config
   config = Config().data["cloudmesh"]

Getting values
--------------

To get values from the configurations, you can call level by level from
top-down config.

.. code:: python

   MONGO_HOST = config["data.mongo.MONGO_HOST"]

Using the Counter file
----------------------

CM4 keeps track of all the VMs running using counters for each VM. The
counter file is located at

.. code:: bash

   ~/.cloudmesh/counter.yaml

Using the counter
-----------------

.. code:: python

   from cloudmesh.cloud.configuration.counter import Counter
   counter = Counter()

The MongoDB Database in ``cloudmesh``
-------------------------------------

We add the database into ``cloudmesh`` with two reasons:

-  provide the information of nodes in different providers.
-  record the experiment executed through cloudmesh, easy for next
   re-execution.

Every time the user use the cloudmesh platform, the server would access
the running MongoDB database, querying the nodes’ information, showing
relative metadata, and then updating all necessary data.

The *MongoDB* would finish below tasks:

-  saving all information:

   1. the nodes’ information queried from cloud service, like name, id,
      status, and other metadata about this node.
   2. saving the executing or executed experiment information, like
      which node we run the experiment, the input, the command, and the
      output.
   3. saving the group information users defined.

-  updating any changes:

   1. the changes updated on the nodes, like stop running node, or start
      stopped node.
   2. the changes updated on the [``cloudmesh4.yaml``], like add new
      nodes.
   3. when the experiment is done, output and experiment status would be
      updated.
   4. new group is created while using ``cms`` will be updated

-  return required information:

   1. return the node information, group information, and experiment
      information when ``cms`` queries them.

Data Scheme in MongoDB
----------------------

There are three types of documents in MongoDB:

-  Node information in ``cloud`` collection. Different cloud service
   providers would return different schemas of node information. It is
   hard to manipulate different nodes’ information into same schema, so
   we decide to dump the return mesaage into MongoDB without any
   changes.

-  Node’s experiment status in ``status`` collection. The document in
   ``status`` collection is going to save the information of experiments
   executed in a node.

   .. code:: text

      {'_id': node_id,
      'status': status,
      'currentJob': job_id,
      'history' : the history of executed experiments in this node}

-  Experiment information in ``job`` collection.

   .. code:: text

      {'_id': experiment_id
      'name': name,
      'status': status,
      'input': input_info,
      'output': output_info,
      'description': description,
      'commands': commands}

-  Group information in ``group`` collection.

   .. code:: text

      {'cloud': cloud,
      'name': name,
      'size': size,
      'vms': list_vms}

Security in MongoDB
-------------------

For data security purpose, we enable the MongoDB security functionality
in ``cms``.

When users first time start the *MongoDB*, they have to add an account
and open an port to access all database in MongoDB. Because we save all
nodes’ information into MongoDB inclduing the *Authorization*
information. If your MongoDB is open to everyone, it is easy for hacker
to steal your information. So you are requried to set the *username* and
*password* for the security purpose.

If you want to learn more about the *Security* in MongoDB, you can visit
this `page <https://docs.mongodb.com/manual/security/>`__ or visit the
brief introduction about the MongoDB

Here is a quick reference about how to `enable MongoDB
Security <https://medium.com/@raj_adroit/mongodb-enable-authentication-enable-access-control-e8a75a26d332>`__
option.

The Virtual Machine Provider
----------------------------

In ``cloudmesh``, we developed the ``cloudmesh-cloud/vm/Vm.py`` class to
implement the operations for different virtual machines from AWS, Azure,
and Chameleon by using the python library `Apache
Libcloud <https://libcloud.apache.org>`__ to interact with cloud service
providers.

The basic functions are:

.. code:: text

   1. start(vm_name) : start the virtual machine with specified name
   2. stop(vm_name, deallocate) : stop the virtual machine with specified name
   3. resume(vm_name) : resume the suspended virtual machine with specified name
   4. suspend(vm_name) : suspend the running virtual machine with specified name
   5. destroy(vm_name) : destroy the virtual machine with specified name
   6. list() : list all virtual machine in your cloud service account
   7. status(vm_name) : show the working status of virtual machine with specified name
   8. info(vm_name) : show all information about the virtual machine with specified name
   9. get_public_ips(vm_name) : return the public ip of the virtual machine with specified name
   10. set_public_ip(vm_name, public_ip): set the public ip for the virtual machine with specified name
   11. remove_public_ip(vm_name) : remove the public ip from virtual machine with specified name

Below we list some sample of running these functions for virtual
machines in AWS, Azure and Openstack.

AWS VM Operations (Yu)
----------------------

Before using the AWS Vm code, user has to update their AWS information
into ``cloudmesh4.yaml`` file in *etc* folder.

The *Libcloud* library has enough methods to support the operations for
managing virtual machines in AWS. We use a ``cloudmesh-cloud/vm/Aws.py``
to create the driver based on the configuration to connect to AWS.

Inherit the *Libcloud* library, we did some modifications on
``AWSDriver`` to extend the operation. The ``create_node`` method would
create a virtual machine in AWS based on the configuration of
``cloudmesh4.yaml`` file

Here are some samples for running these operations by using
``cloudmesh-cloud``:

First, user would create the virtual machine in AWS.

.. code:: bash

   $ cms vm create
   Collection(Database(MongoClient(host=['127.0.0.1:27017'],
              document_class=dict, tz_aware=False, connect=True),
              'cloudmesh'), 'cloud')
   Thread: updating the status of node
   Created base-cloudmesh-yuluo-4
   PING 52.39.13.229 (52.39.13.229): 56 data bytes

   --- 52.39.13.229 ping statistics ---
   1 packets transmitted, 0 packets received, 100.0% packet loss

VM Refactoring
--------------

In addition, in order to offer more flexibilities to our users, we also
developed vmrefactor (``cloudmesh-cloud/vm/VmRefactor.py``) to allow
users to customize the flavors of their running instances and services
in different providers.

1. resize(vm_name, size) : resize the virtual machine with specified
   size object
2. confirm_resize(vm_name) : some providers requires confirmation
   message to complete resize() operation
3. revert(vm_name) : revert a resize operation. Revert the virtual
   machine to previous status
4. rename(vm_name, newname) : rename the virtual machine
5. rebuild(vm_name, image) : rebuild the virtual machine to another
   image/OS with image object.

Currently, major providers usually charge users according to their
usage. It might be finacially wise sometimes to shift between different
service size to reduce unnecessary cost. VmRefactor is designed based on
this idea to help users to achieve higher cost efficiency. VmRefactor
can also help users navigate thier management tasks especially when they
have many different tasks on the run=.
