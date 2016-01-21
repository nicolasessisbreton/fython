from ctypes import *
from fython.fytypes import *

x = Real(value=1)
print(x[:])
x[:] = 10
print(x)

x = Real(value=[1,2,3])
print(x[:])
x[:] = 10
print(x)
print(x.ref[0])
print(x.value)






