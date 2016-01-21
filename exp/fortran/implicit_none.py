import os
from ctypes import *
from numpy import *

c = """
module a
	;implicit none

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')
