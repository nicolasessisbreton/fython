from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer

a = cdll.LoadLibrary('./a.so')

add = a.add
add.argstype = [POINTER(c_float)]
add.restype = c_float

x = c_float(2.5)
r = byref(x)
print(add(r))

tot = a.tot

# scalar
n = 5
t = c_float * n
tot.argstype = [POINTER(t), POINTER(c_int)]
tot.restype = c_float
x = t(*[10,2,3,4,5])
x = byref(x)
y = c_int(n)
y = byref(y)

print(tot(x, y))

# array
mod = a.mod
t = c_float * 3
mod.argstype = [POINTER(t)]
mod.restype = c_void_p
x = t(1, 2, 3)
p = byref(x)
mod(p)
print(x, x[0])
y = np.ctypeslib.as_array(x)
print(y)
y[:]=2
print(2, y)
mod(p)
print(3, y)

# string
s = a.s
t = c_char*4
s.argstype = [POINTER(t)]
s.restype = c_void_p
x = t()
s(byref(x))
print('string', x.raw, x.value)

# global variable
print(c_int.in_dll(a, 'global'))

# string array
svec = a.svec
t = (c_char*4)*3 
svec.argstype = [POINTER(t)]
svec.restype = c_void_p
x = t()
x[0].value = b'xyz'
svec(byref(x))
print(11, x[0].raw)
print(22, x[1].raw)
print(33, x[2].raw)

# global variable after error
print('before error')

err = a.err
err.argstype = [POINTER(c_float)]
err.restype = c_void_p
g = c_float(1)
a.err(byref(g))
print('error val', g.value)

x = c_float(2.5)
r = byref(x)
print('after error', add(r))
