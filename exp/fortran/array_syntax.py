import os
from ctypes import *
from numpy import *

c = """
module a
	
	type AA
		real x(10)
	end type

	type(AA) y(10)
contains

subroutine f() 
	write(*, *) y(1)%x(1)

end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_f_()

