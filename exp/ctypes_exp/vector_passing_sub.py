import os
from ctypes import *
from numpy import *

c = """
module a

contains

subroutine f(x) 
	integer, dimension(2), intent(inout) :: x
	write(*, *) 'entering f'
	write(*, *) 'x at entry', x
	x = x * 10
	write(*, *) 'x before exit', x
	write(*, *) 'exiting f'
end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

f = m.a_mp_f_

t = c_int*2

x = t(1, 1)
print(x[0], x[1])
f( byref(x) )
print(x[0], x[1])