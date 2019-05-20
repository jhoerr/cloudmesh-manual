Code Management
---------------

At this time we recommend and require that you use ``pyCharm`` community
edition or profesional to edit your code. Before committing we like that
you run ``Inspect Code`` on all files that you commit and fix as many
errors as possible including PEP8 format suggestions. It also notifies
you of issues you may not think about while doing other code inspection.

The reason we ask you to do so is that pycharms code inspection is very
good, and that if everyone uses pycharm the format of the code is
uinform and we do not run in to formatting issues.

This will make the review of any code contributed much easier.

Naturally you can use a different editor for your work, but we still ask
you to use pycharm to fix formatting and code inspection before you
commit.

Typically we run a code inspection every week.

Documentation Management
------------------------

To increase readability of the documentation we ask you to try to use 80
character line limits if possible. This is important for better editing
experience in github. A good editor to do this with is emacs withe its
``Esc-q`` command and pycharm with its ``Edit-Wrap Line to`` column or
paragraph features. On macOS this can be called with
``CONTROL-SHIFT-COMMAND-W`` or ``CONTROL-SHIFT-COMMAND-P``

.. todo:: explain how to set the fill paragraph in pycharm to CTRL SHIFT
COMMAND P


Contributing to documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of the documentations are in the ``cloudmesh-manual`` repository which is
automatically cloned when installing the cloudmesh using ``cloudmesh-installer``
. The documentation source files are located in ``docs-source`` folder inside
the ``cloudmesh-manual`` repository.

It's very important to build the documentation locally and test the
modifications before pushing them to the remote. To build the documentation
locally you first, make sure that the proper virtual environment is
activated, then you need to install the requirements and make the
documentation:

.. code:: bash

    cd cloudmesh-manual
    pip install -r requirements.txt
    make doc
    make manual
    make doc
    make view

After this you can open the documentation located at
``cloudmesh-manual/docs/index.html`` in the browser of your choice. Then
after changes and modifications to the documentations, you can build the
documentation locally and see the effect locally using ``make doc`` within
the ``cloudmesh-manual`` folder.

Version Management
------------------

This is only done by Gregor

To create a development version we say

.. code:: bash

    $ make build

To increase the patch number, say

.. code:: bash

    $ make patch

To increase the minor number

.. code:: bash

    $ make minor

The major number will stay to 4, so this is not changed

To create a release say

.. code:: bash

    $ make release

After the release is done the minor number will be increased and the
build number will be reset.
