def into_account(m, age=18):
    a=4
    b=2 
    m = m/0
    return m

import pdb
pdb.runcall(into_account, 7)

>>> def into_account(m, age=18):
...     a=4
...     b=c 
...     m = m/0
...     return m
... 
>>> import pdb;
>>> pdb.runcall(into_account)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.5/pdb.py", line 1576, in runcall
    return Pdb().runcall(*args, **kwds)
  File "/usr/lib/python3.5/bdb.py", line 465, in runcall
    res = func(*args, **kwds)
TypeError: into_account() missing 1 required positional argument: 'm'
>>> pdb.runcall(into_account, 7)
> <stdin>(2)into_account()
(Pdb)