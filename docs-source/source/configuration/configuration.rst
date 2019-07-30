Configuration
=============

The Configuration of cloudmesh is controlled with a yaml file that is
placed in ``~/.cloudmesh/cloudmesh.yaml``. It is created automatically
from the template located at

-  https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/etc/cloudmesh.yaml

You can customize the file while editing it.


Cloudmesh Yaml File Object definitions
--------------------------------------

Getting Values
--------------

We implemented a convenient get method in case you need to look up
some values in the configuration file. For example::

    cms config get cloudmesh.profile
    cms config get cloudmesh.profile.firstname

print information out. While the first points to a dict, it prints
out all the values form that dict, the last is an attribute and just
prints out the attribute and its value.

Setting values
--------------

In addition if you need to set quickly a value in the configuration
file you can do this with::

    cms config set cloudmesh.profile.firstname=Gregor

Will set the firstname in the profiles to Gregor

This command at this time does not work on dicts, so you need to
define each attribute.

Editing Values
--------------

IN case the values in the yaml file are having a TBD the can also be
edit it with our build in command that required you to specify the dict
in which such values occur.

For example, let us assume the value in `cloudmesh.profile.firstname` is
TBD then, the command::

    cms config edit cloudmesh.profile

Can be used to change it.

Advanced Yaml Variables
-----------------------

One of the features of the cloudmesh yaml framework is that it allows
you to use previously defined attributes in the yaml file itself. Thus
if an attribute value contains for example `{cloudmesh.attribute}`
or any environment variable such as `$HOME`, it will find the value for
this dict entry in the yaml file and replace it with its value. For example. let
us assume the yaml file contains::

    cloudmesh:
      profile:
        name: Gregor
      cloud:
        aws:
          username: "{cloudmesh.profile.name}"
          key: ~/.ssh/id_rsa
          dir: $HOME
          current: .

cloudmesh will replace the will result be transformed with::

    cloudmesh:
      profile:
        name: Gregor
      cloud:
        aws:
          username: "Gregor"
          key: /home/gregor/.ssh/id_rsa
          dir: /home/gregor
          current: /home/gregor/github/cm

This feature is naturally very useful for creating templates for users


Profile
-------

The profile defines simple information about you::

  profile:
    firstname: TBD
    lastname: TBD
    email: TBD@sample.edu
    user: TBD
    github: TBD
    publickey: ~/.ssh/id_rsa.pub


Default
-------

The global default is used to identify information about your
experiments and groups that are used throughout your interaction with
cloudmesh::

  default:
    group: cloudmesh
    experiment: base
    cloud: azure
    cluster: clustera

The values can be set with the default command

.. todo:: implement the default command and set values in it. This may
          already be done. we may need to add the dot notation for
          that command so we have one command that can set the general
          default, but also the default for named services.

          a link to the manual page should come here



General Service Attributes
-------------------

Each cloudmesh service must have an attribute ``cm`` with the
following fields. if an attribute contains the value TBD it need sto
be updated. YOu only have to update the providers you like to use, you
can delete the other if you like.

cm
~~

In the ``cm` portion we define elementary information that identifies
the service. This includes The following information

active

    if set to Tru, this cloud is going to be used in cloudmesh, if it
    is set to False it is not activated.  This has the advantage that
    you do not have to remove the service from the yaml file if you do
    not use it

heading

    This field is currently not used, but in future releases this
    field will be use in table or GUIs to be printed when list
    functions are used

label

    This field is typically the same as the entry under which the
    cloud service is filed. IN our case it is aws. It is a convenient
    abbreviation that can be used in your programs.

kind

    This field is the most important field that identified what kind
    of service your cloud is and it will determine based on its name
    how to interact with the service.

    For compute services the following kinds are valid: ``aws``,
    ``azure``, ``google``, ``openstack``

    For storage services the following kinds are valid: ``aws``,
    ``azure``, ``google``, ``openstack``, ``box``

host

    This field is used to identify where to find information about the
    service provider

service

    The type of service. valid values are ``compute``, ``storage``.

::

    cm:
        active: False
        heading: AWS
        host: aws.amazon.com
        label: aws
        kind: aws
        version: 1.0
        service: compute

Compute Cloud Providers
-----------------------

The default yaml file includes templates to configure various clouds.
YOu can change these defaults and provide access to your cloud
credentials to make the management of cloud virtual machines easier.
Templates for AWS, Azure, Google, OpenStack are provided. Specific
templates for Jetstream and Chameleon cloud are included in the example
`cloudmesh.yaml <https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/etc/cloudmesh.yaml>`__.
We list each template next.

We explain in more detail the features of the configuration files for
cloud services.

First all cloud services are listed under the key ``cloud``. You can
add arbitrary compute cloud services with a name you like. You can
even create multiple names that refer to the same cloud but may have
different parameters.  We like to focus on the example for ``aws`` and
explain this in a bit more detail.


The cloudmesh entry for a compute service is divided into three
portions: ``cm``, ``default``, and ``credentials``. The format of the
``cm`` is explained previously.


Default
~~~~~~~

The next category are defaults that can be preset for each
cloud. However defaults are overwritten by the cloudmesh shell
variables. So they are only used once at startup if these defaults are
not already defined by cloudmesh shell. Typically we use them to for
example define values for images and sizes or flavors of images

image

    The name of the default image

size

The size of the default image

credentials
~~~~~~~~~~~

The credentials are dependent on the kind of the cloud and include all
information needed for authenticate and use the cloud service.

As the information is sensitive the file in .cloudmesh holding this
information must be properly protected.

.. note:: We even have a project that encrypts the cloudmesh.yaml
          file, but it is not fully integrated yet.  Future versions
          of cloudmesh will encrypt the information by default.

AWS
~~~

To obtain an account on AWS you can follow our instructions at
:doc:`../accounts/aws`. The configuration file contains the
following::

   cloudmesh:
     ...
     cloud:
       ...
       aws:
         cm:
           active: False
           heading: AWS
           host: aws.amazon.com
           label: aws
           kind: aws
           version: TBD
           service: compute
         default:
           image: 'ami-0f65671a86f061fcd'
           size: 't2.micro'
         credentials:
           region: 'us-west-2'
           EC2_SECURITY_GROUP: 'group1'
           EC2_ACCESS_ID: TBD
           EC2_SECRET_KEY: TBD
           EC2_PRIVATE_KEY_FILE_PATH: '~/.cloudmesh/aws_cert.pem'
           EC2_PRIVATE_KEY_FILE_NAME: 'aws_cert'

Azure
~~~~~

.. todo:: az arm provider this has to be verified. We will likely
          deprecate this for a more elaborate provider

To obtain an account on Azure you can follow our instructions at
:doc:`../accounts/azure`. THe configuration file contains the
following::


   cloudmesh:
     ...
     cloud:
       ...
       azure:
         cm:
           active: False
           heading: AWS
           host: azure.microsoft.com
           label: Azure
           kind: azure_arm
           version: TBD
           service: compute
         default:
           image: 'Canonical:UbuntuServer:16.04-LTS:latest'
           size: 'Basic_A0'
           resource_group: 'cloudmesh'
           storage_account: 'cmdrive'
           network: 'cmnetwork'
           subnet: 'cmsubnet'
           blob_container: 'vhds'
         credentials:
           AZURE_TENANT_ID: 'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
           AZURE_SUBSCRIPTION_ID: 'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
           AZURE_APPLICATION_ID: 'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
           AZURE_SECRET_KEY: TBD
           AZURE_REGION: 'northcentralus'

AZ
~~

.. todo:: AzProvider. Verify it works

This provider leverages the "az" command. and is the preferred az
provider at this time. It has npt yet been fully verified.

To obtain an account on Azure you can follow our instructions at
:doc:`../accounts/azure`. THe configuration file contains the
following::

   cloudmesh
      ...
      cloud:
        ...
        az:
         cm:
           active: False
           heading: AWS
           host: azure.mocrosoft.com
           label: Azure
           kind: azure
           version: TBD
           service: compute
         default:
           image: 'Canonical:UbuntuServer:16.04-LTS:latest'
           size: 'Basic_A0'
           resource_group: 'cloudmesh'
           storage_account: 'cmdrive'
           network: 'cmnetwork'
         credentials:
           resourcegroup: "test"
           location: "eastus"

Google
~~~~~~


To obtain an account on Google you can follow our instructions at
:doc:`../accounts/gooogle`. THe configuration file contains the
following::

   cloudmesh:
     ...
     cloud:
       ...
       google:
         cm:
           active: True
           heading: google
           host: google.cloud.com
           label: google
           kind: google
           version: TBD
           service: compute
         default:
           image: 'Image Name'
           size: 'n1-standard-4'
         credentials:
           datacenter: 'us-central1-a'
           client_email: '<service account>.iam.gserviceaccount.com'
           project: '<Project Name>'
           path_to_json_file: '~/.cloudmesh/<file with credentials>'

OpenStack
~~~~~~~~~

We provide an example on how to use an OpenStack based cloud in
cloudmesh. Please ass the following to your ``cloudmesh.yaml`` file
and replace the values for ``TBD``. Our example uses `Chameleon Cloud
<https://www.chameleoncloud.org/>`__. This is a cloud for academic
research. Certainly you can configure other clouds based on this
template. We have successfully used also clouds in Canada (Cybera),
Germany (KIT), Indiana University (jetstream). TO get started you can
even install your local cloud with devstack and make adjustments.
Please remember you can have multiple clouds in the
``cloudmesh.yaml`` file so you could if you have access to them
integrate all of them.  You will need access to a project and add your
project number to. the credentials.  Example for chameleon cloud::

   cloudmesh:
     ...
     cloud:
       ...
       chameleon:
         cm:
           active: True    
           heading: Chameleon
           host: chameleoncloud.org
           label: chameleon
           kind: openstack
           version: liberty
           service: compute
         credentials:
           OS_AUTH_URL: https://openstack.tacc.chameleoncloud.org:5000/v2.0/tokens
           OS_USERNAME: TBD
           OS_PASSWORD: TBD
           OS_TENANT_NAME: CH-819337
           OS_TENANT_ID: CH-819337
           OS_PROJECT_NAME: CH-819337
           OS_PROJECT_DOMAIN_ID: default
           OS_USER_DOMAIN_ID: default
           OS_VERSION: liberty
           OS_REGION_NAME: RegionOne
           OS_KEY_PATH: ~/.ssh/id_rsa.pub
         default:
           flavor: m1.small
           image: CC-Ubuntu16.04
           username: cc        

Virtual Box
~~~~~~~~~~~

Virtualbox has at this time limited functionality, but creation, ssh,
and deletion of the virtual box is possible.

You can also integrate virtualbox as part of cloudmesh while providing
the following description::

   cloudmesh:
     ...
     cloud:
       ...
       vbox:
         cm:
           active: False            
           heading: Vagrant
           host: localhost
           label: vbox
           kind: vagrant
           version: TBD
           service: compute
         default:
           path: ~/.cloudmesh/vagrant
           image: "generic/ubuntu1810"
         credentials:
           local: True
           hostname: localhost

SSH
~~~

.. todo:: SSH,  STUDENT CONTRIBUTE HERE

Local
~~~~~

.. todo:: Local,  STUDENT CONTRIBUTE HERE

Docker
~~~~~~

.. todo:: Docker,  STUDENT CONTRIBUTE HERE

Storage Providers
-----------------

General description for all storage providers, comment on the
``default:`` and what that does

AWS S3
~~~~~~

It is beyond the scope of this manual to discuss how to get an account
on Google. However we do provide a convenient documentation at
:doc:`../accounts/aws`.


In the ``cloudmesh.yaml`` file, the ‘aws’ section under ‘storage’
describes an example configuration or a AWS S3 storage provider. In
the credentials section under aws, specify the access key id and
secret access key which will be available in the AWS console under AWS
IAM ``service`` -> ``Users`` -> ``Security Credentials``. Container is
the default Bucket which will be used to store the files in AWS
S3. Region is the geographic area like ``us-east-1`` which contains
the bucket.  Region is required to get a connection handle on the S3
Client or resource for that geographic area. Here is a sample::

   cloudmesh:
     ...
     storage:
       aws:
         cm:
           heading: aws
           host: amazon.aws.com
           label: aws
           kind: awsS3
           version: TBD
           service: storage
         default:
           directory: /
         credentials:
           access_key_id: *********
           secret_access_key: *******
           container: name of bucket that you want user to be contained in.
           region: us-east-1

.. todo:: Make credentials more uniform between compute and data


.. _azure-1:

Azure
~~~~~

It is beyond the scope of this manual to discuss how to get an account
on Google. However we do provide a convenient documentation at
:doc:`../accounts/azure`.

The ``cloudmesh.yaml`` file needs to be set up as follows for the
‘azureblob’ section under ‘storage’::

   cloudmesh:
     ...
     storage:
       azureblob:
         cm:
           heading: Azure
           host: azure.com
           label: Azure
           kind: azureblob
           version: TBD
           service: storage
         default:
           directory: /
         credentials:
           account_name: '*****************'
           account_key: '********************************************************************'
           container: 'azuretest'

Configuration settings for credentials in the yaml file can be
obtained from Azure portal.

TODO: MOre information via a pointer to a documentation you create
needs to be added here

In the yaml file the following values have to be changed

-  ``account_name`` - This is the name of the Azure blob storage
   account.
-  ``account_key`` - This can be found under ‘Access Keys’ after
   navigating to the storage account on the Azure portal.
-  ``container`` - This can be set to a default container created under
   the Azure blob storage account.

Google drive
~~~~~~~~~~~~

Due to bugs in the requirements of the google driver code, we have not
yet included it in the Provider code. This needs to be fixed before we
can do this.

It is beyond the scope of this manual to discuss how to get an account
on Google. However we do provide a convenient documentation at
:doc:`../accounts/google`.

The ``cloudmesh.yaml`` file needs to be set up as follows for the
‘gdrive’ section under ‘storage’::

   cloudmesh:
     ...
     storge:
       gdrive: 
         cm: 
           heading: GDrive
           host: gdrive.google.com
           kind: gdrive
           label: GDrive
           version: TBD
           service: storage
         credentials:
           auth_host_name: localhost
           auth_host_port: 
             - ****
             - ****
           auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs"
           auth_uri: "https://accounts.google.com/o/oauth2/auth"
           client_id: *******************
           client_secret: ************
           project_id: ************
           redirect_uris: 
             - "urn:ietf:wg:oauth:2.0:oob"
             - "http://localhost"
           token_uri: "https://oauth2.googleapis.com/token"
         default: 
           directory: TBD

Box
~~~

It is beyond the scope of this manual to discuss how to get an account
on Google. However we do provide a convenient documentation at
:doc:`../accounts/box`.


In the ``cloudmesh.yaml`` file, find the ‘box’ section under ‘storage’.
Under credentials, set ``config_path`` to the path of the configuration
file you created as described in the Box chapter::

   cloudmesh:
     ...
     box:
       cm:
         heading: Box
         host: box.com
         label: Box
         kind: box
         version: TBD
         service: storage
       default:
         directory: /
       credentials:
         config_path: ******************************


Batch
-----

.. todo:: batch, student contribute here


REST
----

TBD

Log File
--------

.. note::  Previous versions of cloudmesh had a sophisticated logging feature.
           This version has this feature not yet made available. Implement it
           and make available. At this time it is not our highest priority.

Log files are stored by default in ``~/.cloudmesh/log`` The directory
can be specified in the yaml file.


Mongo
-----

MongoDB
-------

The cache of cloudmesh is managed in a mongo db database with various
collections. However the user does not have to manage the collections
as this is done for the user through cloudmesh. Before you can use it it
mongo does need to be installed.

If you have not installed mongo, you may try

.. code:: bash

   cms admin mongo install

However, to install it with cms, you must also make sure the following values are
installed in the cloudmesh yaml file::

    ...
    MONGO_PASSWORD: TBD
    ...
    MONGO_AUTOINSTALL: True

The value for the password must not be ``TBD``.

Next you create the database template with authentication with

.. code:: bash

   cms admin mongo create

Now you are ready to use it in cloudmesh. The mongo db can be started
and stopped with the command

.. code:: bash

   $cms admin mongo start
   $cms admin mongo stop

The configuration details are included in the yaml file and looks like::

   cloudmesh:
     ...
        mongo:
          MONGO_AUTOINSTALL: False
          MONGO_BREWINSTALL: False
          LOCAL: ~/local
          MONGO_HOME: ~/local/mongo
          MONGO_PATH: ~/.cloudmesh/mongodb
          MONGO_LOG: ~/.cloudmesh/mongodb/log
          MONGO_DBNAME: 'cloudmesh'
          MONGO_HOST: '127.0.0.1'
          MONGO_PORT: '27017'
          MONGO_USERNAME: 'admin'
          MONGO_PASSWORD: TBD
          MONGO_DOWNLOAD:
            darwin: https://fastdl.mongodb.org/osx/mongodb-osx-ssl-x86_64-4.0.4.tgz
            linux: https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-4.0.4.tgz
            win32: https://fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-4.0.4-signed.msi
            redhat: https://repo.mongodb.org/yum/redhat/7/mongodb-org/4.0/x86_64/RPMS/mongodb-org-server-4.0.4-1.el7.x86_64.rpm


