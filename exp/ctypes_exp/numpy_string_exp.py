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
character(3), dimension(2) :: x = ['abc', 'def']
""")
t = (c_char*3)*2
print(t)
x = t.in_dll(m, 'a_mp_x_')
print(x[0].value, x[1].value)
xx = ctypeslib.as_array(x)