from ctypes import *
from numpy import array

t = c_char * 3
x = t(b'a', b'b', b'c')

x.__array_interface__ = {
		'shape': (),
		'typestr': 'S3',
		'data': (addressof(x), 0),
	}

y = array(x,copy=0) 

print(y)
print(repr(y))
print(x)