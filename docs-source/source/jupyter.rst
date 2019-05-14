Jupyter Integration (proposed)
==============================


.. todo:: The jupyter integration was available in an earlier ersion of
          cloudmesh and we need to make sure that ut also works here.

As cloudmesh provides an API but also is available as command shell it
is very easy to integrate it into jupyter

In this section we describe hw to do this.

Any cms command can be run via the shell

.. code:: bash

    [1] !cms set cloud=AWS
    [2] !cms vm start

API command shell access (proposed)
-----------------------------------

To use a more pythonic apporach you can do

.. code:: python

    import cloudmesh

    script = """
    cms set cloud=AWS
    cms vm start
    """

    cloudmesh.shell(script)

API calls (ok)
--------------

To use the specific API calls, look at the manaul or the tests. To list
for example the flavors of a cloud you can use:

.. code:: python

    from cloudmesh.compute.libcloud.Provider import Provider 
    from cloudmesh.common.Printer import Printer
    from pprint import pprint

    provider = Provider(name="chameleon")
    images= provider.images()

    pprint (images)

To print the information in a noce table you can also use

.. code:: python

    print(Printer.flatwrite(images,
                            sort_keys=("name","extra.minDisk"),
                            order=["name", "extra.minDisk", "updated", "driver"],
                            header=["Name", "MinDisk", "Updated", "Driver"])
         )

The printer has a flatwrite method included that first converts the dict
into a flat dict, where each attribute is changed to a single level dict
by using a period to indicate the indentation of the dicts in case dict
of dicts are used as in our example
