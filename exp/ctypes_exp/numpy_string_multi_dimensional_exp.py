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
character(3), dimension(2, 2) :: x = ['abc', 'def', 'xyz', 'uvw']
""")
t = ((c_char*3)*2)*2
x = t.in_dll(m, 'a_mp_x_')
print(x[0][0].value, x[0][1].value)