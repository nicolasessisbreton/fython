import os
from ctypes import *
from numpy import *

c = """
module aa

contains

subroutine f()
	write(*, *) 11
	contains
end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -c -fpic -o b.o')


