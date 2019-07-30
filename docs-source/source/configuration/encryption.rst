Cloudmesh Yaml file Encryption
==============================

.. warning:: THIS SECTION IS UNDER DEVELOPMENT AND THE CONTENT DESCRIBED IS NOT
             YET FULLY WORKING

.. todo:: verify the entire content of the encryption command



The cloudmesh yaml file can contain some information to simplify
authentication. In order not tos store the file in clear text we have
provided a replacement function for the configuration that allows
encryption of the file with your ssh key. IT is important that your ssh
key is generated with a passphrase. If you do not, even if you encrypt,
the file can without a passphrase decrypted which is the same as having
it in clear text. So make sure tour ssh-key has a passphrase.

Prerequisits
------------

You have an ssh key

Encryption
----------

To encrypt the file, pleas use the command

.. code:: bash

   cms config encrypt 

This command will encrypt your ``cloudmesh.yaml`` file and place it
under ``~/.cloudmesh/cloudmesh.yaml.enc``. It will ask you if you like
to delete the original yaml file.

Decryption
----------

To decrypt the file, pleas use the command

.. code:: bash

   cms config decrypt 

This command will decrypt your ``cloudmesh.yaml.enc`` file and place it
under ``~/.cloudmesh/cloudmesh.yaml.enc.enc``. It will ask you if you
like to delete the original yaml file.

Cloudmesh Integration
---------------------

We have provided a new
``cloudmesh.management.configuration.ConfigCrypt()`` That will be
integrated in future (once verified it works) into the regular
``Config()``

The functionality tht is provided by ``ConfigCrypt()`` includes

-  if ``cloudmesh.yaml`` and ``cloudmesh.yaml.enc`` exist a warning is
   written that both files exist and it recommended in production to
   delete the unencrypted file.

-  if only ``cloudmesh.yaml`` exist a warning is written that an
   unencrypted yaml file is used

-  if only ``cloudmesh.yaml.enc`` exists it is unencrypted and loaded
   into memory. Please note that ``ConfigCrypt()`` just as Config() is
   implemented as Borg class so that the decryption and loading loading
   is conducted only once.

Editing the Configuration file
------------------------------

Editing the configuration file can be done by first decrypting the
file with

.. code:: bash

   TBD

Than you can use your favourite editor to make modifications. Let us
assume this is emacs.

.. code:: bash

   emacs ~/.cloudmesh/cloudmesh.yaml

Once written back quit your editor and encrypt the file with

.. code:: bash

   cms config encrypt

Adding information to the configuration
---------------------------------------

It is also possible to add configurations to the encrypted file while
storing the new values in a temporary yaml file.

Let us assume the temporary file ``./change.yaml`` contains the
following information:

::

   cloudmesh:
     profile:
       firstname: Gregor
       lastname: von Laszewski

Than the command

.. code:: bash

   cms config add ./change.yaml

Will update the existing ``cloudmesh.yaml`` or cloudmesh.yaml.enc\`
file with the provided information. This is taking place regardless if
the yaml file is encrypted or not. If both files exist, both files will
be modified. A warning is however issued if the unencrypted yaml file
exists to remind the user to delete it.

Alternatively the convenient dot notation cloudmesh provides for
configuration files can be used. This is done by having the ending
``txt`` instead of ``yml`` We illustrated this on the following example
where the data is stored in ``change.txt``

::

   cloudmesh.profile.firstname: Gregor
   cloudmesh.profile.lastname: von Laszewski

.. code:: bash

   cms config add ./change.txt

Separating the sensitive information
------------------------------------

As it may be beneficial to separate the sensitive form the non sensitive
information, we also provide a mechanism for authentication with a
merged file. This way you could for example store the sensitive
information on a USB key.

For this to work we specify in the yaml file a field called

.. code:: bash

   cloudmesh:
     encrypted: ~/.cloudmesh/cloudmesh4-secrets.yaml.enc

You can name the file anything you like and you could point it to your
location of the USB key.

in this file we store only the sensitive information such as

.. code:: bash

   cloudmesh.storage.azure.credentials.AZURE_SUBSCRIPTION_ID: 'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

PLease note that we leverage the convenient dot notation cloudmesh
provides for configuration files so we can formulate the value in a
single line>
