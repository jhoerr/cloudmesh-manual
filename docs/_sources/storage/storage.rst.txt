Cloudmesh Multi Cloud Storage Interface
=======================================

Cloudmesh supports multiple cloud storage services. You can access them
via commandline, an API or REST services. A simple abstraction layer
between cloud services and you local computer makes it possible that the
services are accessed the same way. This includes AwsS3, Azure, Google,
and box.

The code is available a cloudmesh module at

-  https://github.com/cloudmesh/cloudmesh-storage

|Version| |License| |Python| |Format| |Status| |Travis|

Installation
------------

.. todo:: the pip install is not yet enabled. Please use the source install
          instead (see Installation instructions).

The storage module can be installed with

.. code:: bash

    pip install cloudmesh-storage

or if you install it from source with the cloudmesh installer

.. code:: bash

    mkdir cm
    cd cm
    cloudmesh-installer git clone storage
    cloudmesh-installer install storage -e


General Storage Command
-----------------------

To view the manual page for the  storage command, type in

.. code:: bash

   cms help storage


.. todo:: include the storage command here

Tos set a storage provider so you do not have to specify it with ``--storage``

we can set it with the set command. We have the following providers to chose
from:

``box``, ``awss3`` , ``awsstorage``, ``azure``, ``google``


.. code:: bash

    cms set storage=awss3


To list the storage service you can say

.. code:: bash

   cms storage list



Configuration
-------------

AWSS3 Cloudmesh Integration
---------------------------

AWS S3 file storage has been integrated with cloudmesh library and is
available for use via commandline. As a first step we need to modify
``cloudmesh.yaml`` config file. Under ‘storage’ section, we need to add
the aws section to specify the parameters used to store files in AWS S3.

In the credentials section under aws, specify the access key id and
secret access key which will be available in the AWS console under
``AWS IAM service`` -> ``Users`` -> ``Security Credentials``.

Container is the default bucket which will be used to store the files in
AWS S3. Region is the geographic area like ``us-east-1`` which contains
the bucket. Region is required to get a connection handle on the S3
Client or resource for that geographic area.

Here is a sample.

.. code:: bash

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
         default:
           directory: TBD
         credentials:
           access_key_id: *********
           secret_access_key: *******
           container: name of bucket that you want user to be contained in.
           region: us-east-1

Cloudmesh AWS Object Storage Interfaces
---------------------------------------

Object Storage is one of the feature in AWS S3 and this feature
integrated with cloudmesh library and is available for use via
commandline.

Follow the below steps:

-  Modify ``cloudmesh.yaml`` config file in ‘cloudmesh-storage’
   section. User need to add required object storage parameters to
   communicate with cloud(AWS S3)

-  In the credentials section under ``awsobjectstore``, add the
   parameter values of access_key_id and secret_access_key, these
   credentials will be gained from appropriate cloud vendor(For ex:
   AWS), in the case of AWS, these will be available which will be
   available in the AWS console under ``AWS IAM service`` -> ``Users``
   -> ``Security Credentials``.

Here is a sample.

.. code:: bash

   cloudmesh:
     ...
     storage:
       objstore:
         cm:
           heading: AWS
           host: aws.com
           label: AWS
           kind: awsobjectstore
           version: 1.0
         default:
           directory: AWS
         credentials:
           region: ""
           access_key_id: ""
           secret_access_key: "" 

Create Object Directory
-----------------------

.. code:: bash

   cms storage create /base_path/targetdir

Put
---

The put command uploads object from your local system to AWS S3 object
storage

.. code:: bash

   cms storage put ~/.cloudmesh/objstore/sourcedir /base_path/targetdir --recursive

Get
---

The put command retrieve or download a object from AWS S3 object storage

.. code:: bash

   cms storage get /bucket_name/src ~/.cloudmesh/objstore/dest --recursive

List
----

The list command lists all the contents of a cloud object details. If
the recursive option is specified, it will list the contents of all the
nested objects information

.. code:: bash

   cms storage list /bucket_name/dest --recursive

Delete
------

The delete command can delete objects on cloud storage. Once object
deletes it will never be rollback and delete applicable to nested
objects when function ``--recursive`` used. Deleting a folder will
delete its contents as well (including the sub-directories).

.. code:: bash

   cms storage delete /bucket_name/est --recursive

Storage functions overview
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create dir
~~~~~~~~~~

This command helps to create a new directory on AWS S3. You must specify
the full path of the new directory you would like to create.

.. code:: bash

   cms storage --storage='aws' create dir /base_path/targetdir

.. _put-1:

Put
~~~

The put command uploads files from your local host to the S3.

.. code:: bash

   cms storage put ~/.cloudmesh/storage/sourcedir /base_path/targetdir --recursive

Source for this command could be either a file or directory.

If you specify a file as the source, the file will be uploaded if no
such file exists on the cloud or updated if a copy already exists on the
cloud.

If the source is a directory, you can choose to specify the recursive
option to upload the files in the sub-directories in the source as well
to the target directory in S3. If the recursive option is not specified,
only the files in the source directory will be uploaded to the target
directory and the sub-directories will be ignored.

.. _get-1:

Get
~~~

The get command downloads files from S3 to your local host.

.. code:: bash

   cms storage get /base_container/sourcedir ~/.cloudmesh/storage/targetdir --recursive

Source for this command could be either a file or directory.

If you specify a file as the source, you need to specify the full path
of file including the file name where you want the file to be
downloaded. In case you do not specify the file name and only give the
target directory, then the file will be downloaded with the same name as
present on S3.

If the source is a directory, you can choose to specify the recursive
option to download files in the sub-directories in the source as well to
the target directory in your local host. If the recursive option is not
specified, only the files in the source directory will be downloaded to
the target directory and the sub-directories will be ignored.

Search
~~~~~~

The search command helps to search for a particular file within a
directory.

If recursive options is specified, Cloudmesh will search for the file in
all sub-directories of the original directory as well.

To search for a file at the root, pass an empty string or / as the
target dir.

.. code:: bash

   cms storage search /base_path/targetdir testfile.txt --recursive

Note that for the Box storage provider, objects are only indexed every 5
to 10 minutes and will not show up in a search until they have been
indexed.

.. _list-1:

List
~~~~

The list command lists all the contents of a cloud directory. If the
recursive option is specified, it will list the contents of all
sub-directories as well.

.. code:: bash

   cms storage list /base_path/targetdir --recursive

.. _delete-1:

Delete
~~~~~~

The delete command can delete files or folders from your cloud file
storage. Deleting a folder will delete its contents as well (including
the sub-directories).

.. code:: bash

   cms storage delete /base_path/targetdir --recursive

Pytests
-------

Generic Tests
~~~~~~~~~~~~~

We have developed a number of simple pytests that can be called. To see
the list of Pytests go to our directory

-  https://github.com/cloudmesh/cloudmesh-storage/tree/master/tests

We also developed a general pytest that works across providers and can
be invoked as follows

.. code:: bash

   cms set storage=box
   pytest -v --capture=no tests/test_storage.py

   cms set storage=azure
   pytest -v --capture=no tests/test_storage.py

   cms set storage=gdrive
   pytest -v --capture=no tests/test_storage.py

   cms set storage=awss3
   pytest -v --capture=no tests/test_storage.py

Provider Specific Pytests
~~~~~~~~~~~~~~~~~~~~~~~~~

Open a terminal and navigate to the cloudmesh-storage directory. Enter
the following command to run pytests:

.. code:: bash

   pytest -v --capture=no tests/test_storage_box.py
   pytest -v --capture=no tests/test_azure.py
   pytest -v --capture=no tests/test_storage_aws.py

TODO: rename to

-  test_storage_azure.py

General features
----------------

How to set up the authentication to a specific service is discussed in
later sections

TODO: Provide a simple programming example with the general provider

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

TBD

.. code:: bash

   cms set storage=azure
   cms storage list

Programming Interface
~~~~~~~~~~~~~~~~~~~~~

TBD

Cloudmesh Storage provides a simple programming API interface that you
can use. We highlight a simple example for storing and retrieving a
file form a storage provider.

We assume the files at the given path exist

.. code:: python

   import cloudmesh.storage.provider.Provider as Provider
   from cloudmesh.common.util import path_expand
   from pprint import pprint

   provider = Provider(service="azure")
   src = path_expand("~/.cloudmesh/storage/test/a/a.txt")
   dst = "/"
   result = provider.put(src, dst)
   # The result will be a dict of the information which you can print with

   pprint(result)

.. _pytests-1:

Pytests
~~~~~~~

Script to test the GDrive service can be accessed under tests folder
using the following pytest command.

TODO rename to test_storage_gdrive.py

.. code:: bash

   pytest -v --capture=no tests/test_gdrive.py

Virtual Directory
-----------------

The virtual directory has been developed to mirror the linux directory
commands. File links in the virtual directory point to files on storage
providers, which can be retrieved using the virtual directory.

Configuration
~~~~~~~~~~~~~

The credentials for the virtual directory are the same as for the admin
mongo command. See the Mongo section for details.

.. _pytests-2:

Pytests
~~~~~~~

The vdir command can be tested as follows:

.. code:: bash

   pytest -v --capture=no tests/test_vdir.py

Google drive
------------

The Google Drive API needs the following two 2 credentials files. \*
``client_secret.json`` \* ``google-drive-credentials.json``

If we run the Google Drive ``Provider.py`` for the **First time** then
the required keys, tokens are taken from the ``cloudmesh.yaml`` file
and creates a ``client_secret.json`` file in the following path
``~/.cloudmesh/gdrive/``

The ``Authentication.py`` creates a ``.credentials`` folder under the
following path ``~/.cloudmesh/gdrive/`` if it does not exist and creates
a ``google-drive-credentials.json`` file under the following folder
``~/.cloudmesh/gdrive/.credentials/``

So, for the **First time** browser will be opened up automatically and
asks for the Google Drive(gmail) credentials i.e., login email and
password. If you provide these 2 then the Authentication step is
completed and then it will create the ``google-drive-credentials.json``
and place it in ``~/.cloudmesh/gdrive/.credentials/`` folder.

These steps are to be followed for the first time or initial run. Once
it is done then our program is set. After these steps then the program
will run automatically by using these credentials stored in the
respective files.

Note
~~~~

The Google Drive API accepts these 2 files in the form of **.json file
format** and not in the form of a dictionary.

Links
~~~~~

Link for additional information:

-  https://github.com/cloudmesh-community/sp19-516-130/blob/master/gdrive.md

.. |Version| image:: https://img.shields.io/pypi/v/cloudmesh-storage.svg
   :target: https://pypi.python.org/pypi/cloudmesh-storage
.. |License| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://github.com/cloudmesh/cloudmesh-storage/blob/master/LICENSE
.. |Python| image:: https://img.shields.io/pypi/pyversions/cloudmesh-storage.svg
   :target: https://pypi.python.org/pypi/cloudmesh-storage
.. |Format| image:: https://img.shields.io/pypi/format/cloudmesh-storage.svg
   :target: https://pypi.python.org/pypi/cloudmesh-storage
.. |Status| image:: https://img.shields.io/pypi/status/cloudmesh-storage.svg
   :target: https://pypi.python.org/pypi/cloudmesh-storage
.. |Travis| image:: https://travis-ci.com/cloudmesh/cloudmesh-storage.svg?branch=master
   :target: https://travis-ci.com/cloudmesh/cloudmesh-storage
