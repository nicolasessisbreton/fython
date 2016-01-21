from ctypes import *
from fython.fytypes import *

x = Char(size=3, value='abc')
print(x[:])
x[:] = 'xyz'
print(x)

x = Char(size=3, value=['abc','def','hij'])
print(x[:])
x[:] = 'x'
print(x)
print(x.ref[0])
print(x.value)

