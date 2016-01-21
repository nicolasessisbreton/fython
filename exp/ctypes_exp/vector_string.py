import os
from ctypes import *
from numpy import *

c = """
module a
character(3), dimension(2) :: x = ['abc', 'def']
end module
"""
open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

t = (c_char*3)*2
x = t.in_dll(m, 'a_mp_x_')
print(x[0].value, x[1].value)
print('{:s}'.format(x[0].value.decode('utf-8')))