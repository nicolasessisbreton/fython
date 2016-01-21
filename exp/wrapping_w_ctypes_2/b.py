"""
ifort a.f90 -shared -fpic -o a.so
stat a.so
nm -D a.so

"""
from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer

a = cdll.LoadLibrary('./a.so')

add = a.a_mp_add_wo_bind_
add.argstype = [POINTER(c_float)]
add.restype = c_float

x = c_float(2.5)
r = byref(x)
print(111, add(r))

tot = a.tot

# scalar
n = 5
t = c_float * n
tot.argstype = [POINTER(t), POINTER(c_int)]
# tot.restype = c_float
x = t(*[10,2,3,4,5])
x = byref(x)
y = c_int(n)
y = byref(y)

r = tot(x, y)
print('tot', r, type(r), dir(r))

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
s = a.a_mp_s_wo_bind_
t = c_char*30
s.argstype = [POINTER(t)]
s.restype = c_void_p
x = t()
x.value = b'abc'
s(byref(x))
print('string', x.raw, x.value)

# global variable
global_int = c_int.in_dll(a, 'global')
print(dir(global_int))
print('global value', global_int)
global_int.value = 10
a.add(byref(c_float(1)))
print('global value after set', global_int)
print('global value in so', c_int.in_dll(a, 'global'))

# global vec
t = c_int*2
g = t.in_dll(a, 'global_vec')
print((g), g[0], g[1])
g[1] = 10
g = t.in_dll(a, 'global_vec')
print(g[0], g[1])
print(c_float, c_float*1, (c_float*2)*4, c_float(1))

# string array
svec = a.a_mp_svec_wo_bind_
t = (c_char*3)*4 
svec.argstype = [POINTER(t)]
svec.restype = c_void_p
x = t()
x[0].value = b'xy1'
x[1].value = b'xy2'
x[2].value = b'xy3'
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
