import os

os.system('rm -rf *.mod *.o *.so')

c = """
module a
integer :: x

end module
"""
open('a.f90','w').write(c)
os.system('ifort a.f90 -c -fpic')

c="""
module b
use a

contains

subroutine f()
	int y
	y = a_mp_x_ + 1
end subroutine

end module
"""
open('b.f90','w').write(c)
os.system('ifort b.f90 -c -fpic')

os.system('ifort -shared a.o b.o -o a.so')


os.system('nm -D a.so')

