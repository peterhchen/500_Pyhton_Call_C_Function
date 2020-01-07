from ctypes import *
# libfun loaded into the python file using fun.myFunction().
# C Function can be accessed.
fun = CDLL ("./libfun.so")
# passed in ctypes.
val1 = fun.myFunction (10)
print ('val1:', val1)
val2 = fun.myFunction (8)
print ('val2:', val2)
