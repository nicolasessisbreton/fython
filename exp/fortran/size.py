import os
from ctypes import *
from numpy import *

c = """
module a

contains 

subroutine g()
	integer x(10)
	write(*, *) size(x), size(x+10+8)
end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_g_()

