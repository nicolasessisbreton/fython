import os
from ctypes import *
from numpy import *

c = """
module a


type B
	real x
end type

type(B) y


contains

function f() result(r)
	type(B) r
	r.x = 10
end function

function g() result(r)
	type(B) x
	real r
	x = f()
	r = x.x
	write(*, *) r 
end function 

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_g_()

