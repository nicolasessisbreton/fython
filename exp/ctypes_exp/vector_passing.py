import os
from ctypes import *
from numpy import *

c = """
module a

contains

function f(x) result(r) bind(c)
	integer, dimension(2), intent(in) :: x
	integer, dimension(2) :: r
	write(*, *) 'entering f'
	r = x * 10
	write(*, *) 'exiting f'
end function

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

# os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

# f = m.a_mp_f_
f = m.f

t = c_float*2
p = POINTER(t)

f.argstype = [p]
# f.restype = c_void_p

x = t(1, 2)

print( f( byref(x) ) )
