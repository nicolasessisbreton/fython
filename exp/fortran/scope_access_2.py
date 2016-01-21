import os
from ctypes import *
from numpy import *

c = """
module a


type B
	real x
end type

contains

function g() result(r)
	type(B), dimension(10) :: x
	x(1).x = 10
	r = x(1).x
	write(*, *) r
end function 

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_g_()

