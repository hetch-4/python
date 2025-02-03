#module is a file contining python definations and statement
#a file with a suffix py


import  fibo        #imports definitions from fibo.py
fibo.fib(1000)      #calls 'fib()' a function from fibo.py


from fibo import fib, fib2      #import the statement from the modules directly
fib(500)

import fibo as fib          #imports fibo but now is available as fib
fib.fib(500)

from fibo import fib as fibonacci  #imports statement fib from fibo now availble as fibonacci
fibonacci(500)

        #built in modules
import sys
print(sys.path)     #specifies the path of a directory
# sys.ps1 = '>>>'            these two define primary snd secondry prompt:
#sys.ps1 = '...'            the two are only defined when the intepretr is in interactive mode

# The  'dir()' Function 
#  finds out which names a module defines
import fibo, sys
print(dir(fibo))