import os
from ctypes import *
from numpy import *

c = """
module a

contains
	subroutine f(x)
		int x
		write(*, *) 1, 2, x
	end subroutine
end module
"""
open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

m = cdll.LoadLibrary('./a.so')

m.__getattr__('a_mp_f_')(byref(c_int(10)))