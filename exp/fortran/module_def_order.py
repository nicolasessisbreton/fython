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

subroutine f(n, x)
	interface
		function f()
			real f
		end function 
	end interface
	
	real x(n)
	int n
	write(*, *) 11, g()
	contains
end subroutine

function g()
	real g
	g = 22
end function 

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_f_()

