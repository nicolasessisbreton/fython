import os
from ctypes import *
from numpy import *

c = """
module b
	integer :: xb = 3
end module

module a
	use b
	integer :: xa = 2
end module

module c
	use b
	use a
	integer :: xc = 1
	contains
	subroutine f()
		write(*, *) xc, xa, xb
	end subroutine
end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.c_mp_f_()

