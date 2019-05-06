
# ######################################################################
# Arguments
# ######################################################################
# {'--kind': 'rst', '--noheader': False, 'COMMAND': 'image'}
# ######################################################################

image
=====

::

    Usage:
        image list [NAMES] [--cloud=CLOUD] [--refresh] [--output=OUTPUT] [--query=QUERY]

    Options:
       --output=OUTPUT  the output format [default: table]
       --cloud=CLOUD    the cloud name
       --refresh        live data taken from the cloud

    Description:
        cm image list
        cm image list --output=csv
        cm image list 58c9552c-8d93-42c0-9dea-5f48d90a3188 --refresh

