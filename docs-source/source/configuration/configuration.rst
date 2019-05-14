Configuration
=============

The Configuration of cloudmesh is controled with a yaml file that is
placed in ``~/.clloudmesh/cloudmesh4.yaml``. It is created automatically
from the templace located at

-  https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/etc/cloudmesh4.yaml

You can customize the file in your local directory.

MongoDB
-------

The cache of cloudmesh is managed in a mongo db database with various
collections. However the user does not have to manage thes collections
as this is done for the user through cloudmesh. Before you can use it it
mongo does need to be installed.

If you have not installed mongo, you may try

.. code:: bash

   cms admin mongo install

Next you create the database template with authentication with

.. code:: bash

   cms admin mongo create

Now you are ready to use it in cloudmesh. The mongo db can be started
and stoped with the command

.. code:: bash

   $cms admin mongo start
   $cms admin mongo stop

The configuration detals are included in the yaml file.

Compute Cloud Providers
-----------------------

The default yaml file includes templates to configure various clouds.
YOu can change these defaults and provide access to your cloud
credentials to make the management of cloud virtual machines easier.
Templates for AWS, Azure, Google, OpenStack are provided. Specific
templates for Jetstream and Chameleopn cloud are included in the example
`cloudmesh4.yaml <https://github.com/cloudmesh/cloudmesh-cloud/blob/master/cloudmesh/etc/cloudmesh4.yaml>`__.
We list each template next.

AWS
~~~

It is beyond the scope of this manual to discuss how to get an account
on Aws. However we do provide a convenient documentation at ??

.. todo:: provide a link to the aws account creation documentation in
          this manual

::

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

It is beyond the scope of this manual to discuss how to get an account
on Azure. However we do provide a convenient documentation at ??

.. todo:: provide a link to the azure account creation documentation in
          this manual



::

   cloudmesh:
     ...
     cloud:
       ...
       azure:
         cm:
           active: False
           heading: AWS
           host: azure.mocrosoft.com
           label: Azure
           kind: azure_arm
           version: TBD
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

::

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

It is beyond the scope of this manual to discuss how to get an account
on Google. However we do provide a convenient documentation at ??

.. todo:: provide a link to the google account creation documentation in
          this manual

::

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
cloudmesh. Please ass the following to your ``cloudmesh4.yaml`` file and
replace the values for ``TBD``. Our example uses `Chameleon
Cloud <https://www.chameleoncloud.org/>`__. This is a cloud for academic
research. Certainly you can configure other clouds based on this
template. We have successfully used also clouds in Canada (Cybera),
Germany (KIT), Indiana University (jetstream). TO get started you can
even install your local cloud with devstack and make adjustements.
Please remember you can have multiple clouds in the ``cloudmesh4.yaml``
file so you could if you have access to them integrate all of them.

Example for chameleon cloud:

-  You will need access to a project and add your project nump=ber to
   the credentials.

::

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
the following description:

::

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
on Google. However we do provide a convenient documentation at ??

.. todo:: provide a link to the aws account creation documentation in
          this manual


In the ``cloudmesh4.yaml`` file, the ‘aws’ section under ‘storage’
describes an example configuration or a AWS S3 storage provider. In the
credentials section under aws, specify the access key id and secret
access key which will be available in the AWS console under AWS IAM
``service`` -> ``Users`` -> ``Security Credentials``. Container is the
default Bucket which will be used to store the files in AWS S3. Region
is the geographic area like ``us-east-1`` which contains the bucket.
Region is required to get a connection handle on the S3 Client or
resource for that geographic area. Here is a sample.

TODO: Make credentials more uniform between compute and data

::

   storage:
       aws:
         cm:
           heading: aws
           host: amazon.aws.com
           label: aws
           kind: awsS3
           version: TBD
         default:
           directory: /
         credentials:
           access_key_id: *********
           secret_access_key: *******
           container: name of bucket that you want user to be contained in.
           region: Specfiy the default region eg us-east-1

.. _azure-1:

Azure
~~~~~

It is beyond the scope of this manual to discuss how to get an account
on Google. However we do provide a convenient documentation at ??

.. todo:: provide a link to the azure  account creation documentation in
          this manual. amke sure it works for vms and storage

The ``cloudmesh4.yaml`` file needs to be set up as follows for the
‘azureblob’ section under ‘storage’.

::

   cloudmesh:
     .........
     storage:
       azureblob:
         cm:
           heading: Azure
           host: azure.com
           label: Azure
           kind: azureblob
           version: TBD
         default:
           directory: /
         credentials:
           account_name: '*****************'
           account_key: '********************************************************************'
           container: 'azuretest'

Configuration settings for credentials in the yaml file can be obtained
from Azure portal.

TODO: MOre information via a pointer to a documentation you create needs
to be added here

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

The ``cloudmesh4.yaml`` file needs to be set up as follows for the
‘gdrive’ section under ‘storage’.

::

   storge:
       gdrive: 
         cm: 
           heading: GDrive
           host: gdrive.google.com
           kind: gdrive
           label: GDrive
           version: TBD
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
on Google. However we do provide a convenient documentation at ??

.. todo:: provide a link to the box account creation documentation in
          this manual


In the ``cloudmesh4.yaml`` file, find the ‘box’ section under ‘storage’.
Under credentials, set ``config_path`` to the path of the configuration
file you created as described in the Box chapter:

::

   box:
     cm:
       heading: Box
       host: box.com
       label: Box
       kind: box
       version: TBD
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
-------------------

.. note::  Previos versions of cloudmesh had a sophisticated logging feature.
           This version has this feature not yet made available. Implement it
           and make avialable. At this time it is not our highest priority.

Log files are stored by default in ``~/.cloudmesh/log`` The directory
can be specified in the yaml file.


