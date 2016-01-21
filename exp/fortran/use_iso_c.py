import os

c = """
module z6e229112f 

use iso_c_binding, only: c_float,  c_int

contains
	subroutine z6e229112f_main()
		write(*, "(a)") '1'
	end subroutine
end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')


