import os

c = """
module a

int x
int y

public :: x
private :: y

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

