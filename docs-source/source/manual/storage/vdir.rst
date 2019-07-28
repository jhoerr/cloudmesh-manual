'CMShell' object has no attribute 'do_vdir'
Traceback (most recent call last):
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/shell/shell.py", line 366, in onecmd
    return func(arg)
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/shell/command.py", line 103, in new
    func(instance, args, arguments)
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/man/command/man.py", line 123, in do_man
    data = self._get_help(entry)
  File "/Users/grey/Desktop/github/cloudmesh-community/cm/cloudmesh-cmd5/cloudmesh/man/command/man.py", line 20, in _get_help
    h = eval("self.do_{what}.__doc__".format(what=what))
  File "<string>", line 1, in <module>
AttributeError: 'CMShell' object has no attribute 'do_vdir'

Timer: 0.0143s (man vdir --format=rst)
