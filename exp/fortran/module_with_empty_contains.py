import os
from ctypes import *
from numpy import *

c = """
module a

contains

subroutine f()
	write(*, *) 11
	contains
end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_f_()

