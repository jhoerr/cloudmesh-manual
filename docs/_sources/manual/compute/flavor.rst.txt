
# ######################################################################
# Arguments
# ######################################################################
# {'--kind': 'rst', '--noheader': False, 'COMMAND': 'flavor'}
# ######################################################################

flavor
======

::

    Usage:
        flavor list [NAMES] [--cloud=CLOUD] [--refresh] [--output=OUTPUT]


    Options:
       --output=OUTPUT  the output format [default: table]
       --cloud=CLOUD    the cloud name
       --refresh        refreshes the data before displaying it

    Description:

        This lists out the flavors present for a cloud

    Examples:
        cm flavor refresh
        cm flavor list
        cm flavor list --output=csv
        cm flavor list 58c9552c-8d93-42c0-9dea-5f48d90a3188 --refresh

        please remember that a uuid or the falvor name can be used to
        identify a flavor.

Timer: 0.0150s (man --kind=rst flavor)
