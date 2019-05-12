
# ######################################################################
# Arguments
# ######################################################################
# {'--kind': 'rst', '--noheader': False, 'COMMAND': 'batch'}
# ######################################################################

'CMShell' object has no attribute 'do_batch'
Traceback (most recent call last):
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/shell/shell.py", line 284, in onecmd
    return func(arg)
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/shell/command.py", line 102, in new
    func(instance, args, arguments)
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/man/command/man.py", line 125, in do_man
    data = self._get_help(entry)
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/man/command/man.py", line 26, in _get_help
    h = eval("self.do_{what}.__doc__".format(what=what))
  File "<string>", line 1, in <module>
AttributeError: 'CMShell' object has no attribute 'do_batch'

