from ctypes import *
from numpy.ctypeslib import as_array
from numpy import array

t = c_char * 3
tv = t * 2

x = tv(t(b'a', b'b', b'c'), t(b'd', b'e', b'f'))

x.__array_interface__ = {
		'version': 3,
		'__ref': x,
		'shape': (2,),
		'typestr': 'S3',
		'data': (addressof(x), False),
		'strides': None,
	}

y = array(x,copy=0) 


y[0] = 'xyz'
print(y, y[0], x[0].raw)