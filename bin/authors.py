#!/usr/bin/env python
from __future__ import print_function
import subprocess
import textwrap

debug = False

names = []

for d in [".",
          "../cloudmesh-cmd5",
          "../cloudmesh-common",
          "../cloudmesh-sys",
          "../cloudmesh-openapi",
          "../cloudmesh-emr",
          "../cloudmesh-cloud",
          "../cloudmesh-storage"]:
    try:
        lines = subprocess.check_output(["git", "shortlog", "-s"], cwd=d).decode('ascii', 'ignore').split("\n")
        for line in lines[:-1]:
            if debug:
                print (d, line)
            names.append("*" + line.strip().split("\t")[1] + "*")
    except:
        pass



names = list(set(names))

names.sort()

name_string = '\n    '.join(textwrap.wrap(', '.join(names), 79, initial_indent="    "))

'''

print("# Contributors")
print()

msg = """Contributors are sorted by the first letter of their combined
Firstname and Lastname and if not available by their github ID.

Please, note that the authors are identified through git logs in
addition to some contributors added by hand. The git repository from
which this document is derived contains more than the documents
included in this document. Thus not everyone in this list may have
directly contributed to this document. However if you find someone
missing that has contributed (they may not have used this particular
git) please let us know. We will add you.

The contributors that we are aware of include:

"""

print("\n".join(textwrap.wrap(msg, 79)))
print()
'''
print()
print (name_string)
print()
