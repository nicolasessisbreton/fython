import os
from ctypes import *
from numpy import *

c = """
module a

contains

subroutine f() 
	int x
	x = 0
	if (.not. x) then
		write(*, *) 1
	else
		write(*, *) 2
	end if
end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_f_()

