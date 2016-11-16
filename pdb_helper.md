#PDB helper


## Help

'''
    (Pdb) help

    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         list      q        rv       undisplay
    a      cl         debug    help      ll        quit     s        unt
    alias  clear      disable  ignore    longlist  r        source   until
    args   commands   display  interact  n         restart  step     up
    b      condition  down     j         next      return   tbreak   w
    break  cont       enable   jump      p         retval   u        whatis
    bt     continue   exit     l         pp        run      unalias  where

    Miscellaneous help topics:
==========================

'''

## Commands

### EOF

1. Handles the receipt of EOF as a command.
'''
	(Pdb) EOF

	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/usr/lib/python3.5/bdb.py", line 52, in trace_dispatch
	    return self.dispatch_return(frame, arg)
	  File "/usr/lib/python3.5/bdb.py", line 96, in dispatch_return
	    if self.quitting: raise BdbQuit
	bdb.BdbQuit
'''

### a(rgs)

1. Print the argument list of the current function.
2. syntaxt: a | args
'''
    >>> def into_account(m, age=18):
    ...     a=4
    ...     b=c
    ...     m = m/0
    ...     return
    ...
    >>> import pdb
    >>> pdb.runcall(into_account, 4)
    > <stdin>(2)into_account()
    (Pdb) a
    m = 4
    age = 18
    (Pdb) args
    m = 4
    age = 18
'''

### alias

### break

###

1. Print a stack trace, with the most recent frame at the bottom.
        An arrow indicates the "current frame", which determines the
        context of most commands.  'bt' is an alias for this command.
2. Where | w | bt
'''
    >>> def into_account(m, age=18):
    ...     a=4
    ...     b=c
    ...     m = m/0
    ...     return
    ...
    >>> import pdb
    >>> pdb.runcall(into_account, 4)
    (Pdb) w
      /usr/lib/python3.5/bdb.py(465)runcall()
    -> res = func(*args, **kwds)
    > <stdin>(2)into_account()
    (Pdb) where
      /usr/lib/python3.5/bdb.py(465)runcall()
    -> res = func(*args, **kwds)
    > <stdin>(2)into_account()
    (Pdb)
'''

### c(ont(inue))

1. Continue execution, only stop when a breakpoint is encountered.


### cl(ear)

1. With a space separated list of breakpoint numbers, clear
        those breakpoints.  Without argument, clear all breaks (but
        first ask confirmation).  With a filename:lineno argument,
        clear all breaks at that line in that file.

### commands

### condition

1. Set a new condition for the breakpoint, an expression which
        must evaluate to true before the breakpoint is honored.  If
        condition is absent, any existing condition is removed; i.e.,
        the breakpoint is made unconditional.

### code

1. Enter a recursive debugger that steps through the code
        argument (which is an arbitrary expression or statement to be
        executed in the current environment).
2.


### disable

### display


### down

1. Move the current frame count (default one) levels down in the
        stack trace (to a newer frame).
2. down | d


### enable

1. Enables the breakpoints given as a space separated list of
        breakpoint numbers.

### exit

1. Quit from the debugger. The program being executed is aborted.
2. q(uit) | exit

'''
    >>> quit()
    guinslym@guinslym-ER883AA-ABA-m7470n:~$ python
    Python 3.5.2 (default, Sep 10 2016, 08:21:44)
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> def into_account(m, age=18):
    ...     a=4
    ...     b=c
    ...     m = m/0
    ...     return m
    ...
    >>> import pdb
    >>> pdb.runcall(into_account, 7)
    > <stdin>(2)into_account()
    (Pdb) q
    >>> q
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'q' is not defined
    >>>
'''


### help

1. Without argument, print the list of available commands.
        With a command name as argument, print help about that command.
        "help pdb" shows the full pdb documentation.
        "help exec" gives help on the ! command.

2. help | h

### ignore

### interact

### jump
### list
### longlist
### next
### pp
### quit
### restart
### return
### retval
### run
### source
### step
### tbreak
### unalias
### undisplay
### until
### up
### whatis
### where
### pdb
### exec



helper:
http://stackoverflow.com/questions/14296603/trace-an-arbitrary-python-command-issued-in-pdb
