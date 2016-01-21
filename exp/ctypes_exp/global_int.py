import os
from ctypes import *
from numpy import *


def f(s):
	global m
	c = """
module a
{:s}
end module
"""
	c = c.format(s)
	open('a.f90','w').write(c)

	os.system('ifort a.f90 -shared -fpic -o a.so')

	os.system('nm -D a.so')

	m = cdll.LoadLibrary('./a.so')

f("""
integer :: x = 10
integer, dimension(2) :: y = [20, 30]
""")
x = c_int.in_dll(m, 'a_mp_x_')
print(x.value)
x.value = 100
x = c_int.in_dll(m, 'a_mp_x_')
print(x.value)


t = c_int*2
x = t.in_dll(m, 'a_mp_y_')
print(x[0], x[1])
x[0] = 200
x[1] = 300
x = t.in_dll(m, 'a_mp_y_')
print(x[0], x[1])


