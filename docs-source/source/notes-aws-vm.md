# Virtual machine Management

* <http://cloudmesh.github.io/cmd3/man/man.html#vm>
* There is also a newer version of cloudmesh, that we have not
  implemented all of this logic but it uses cmd5

Virtual machines are managed with the vm command



## Status

Looks at the system sattus of mongo and other cms vm stuff

```
cms admin status
```

## Backup 

makes backup of the data in mongo

```
cms admin mongo save [--file=FILE]
cms admin mongo load [--file=FILE]
```



## Group command


```bash
cms group list [--group=GROUP]
cms group delete [--group=GROUP]
cms group add VMNAMES
cms group=cluster1
```

## Vm command

```bash
cms cloud=aws
cms vm list

# all subsequent commands are added to the group. The last group is set to 
# group1, a group can have arbitrary resources in it vms, files, ...
# commands applied to last vm 
cms vm start [--cloud=CLOUD]


cms vm stop [--cloud=CLOUD]
cms vm info [--cloud=CLOUD]
cms vm delete [--cloud=CLOUD]
cms vm suspend [--cloud=CLOUD]
```


#### Check instances

```
cms vm check instance <label_name> process_name <process>
```
check the running process in the instance. For example:
```
  cms vm check isntance aws_a process_name test
```

