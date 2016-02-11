import os
from ctypes import *
from numpy import *

c = """
module a

contains
	subroutine f(x, y)
		real :: x, y
	end subroutine

	subroutine g()
		call f(y=1., x=x)
	end subroutine
end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')
