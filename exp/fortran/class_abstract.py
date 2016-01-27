import os
from ctypes import *

c = """
module a

  type :: Base
	integer x
	contains
	procedure :: add => base_add
  end type

  type, extends(Base) :: Derived
	contains
	procedure :: add => derived_add
  end type

contains

  subroutine base_add(self, value)
	class(Base), intent(inout) :: self
	integer, intent(in) :: value
	self%x = value
  end subroutine

  subroutine derived_add(self, value)
	class(Derived), intent(inout) :: self
	integer, intent(in) :: value
	self%x = value
  end subroutine

  subroutine f(s, x)
  	class(Base), intent(inout) :: s
  	integer, intent(in) :: x
  	s%x = x
  end subroutine

  subroutine test()
  	type(Base) :: b
  	type(Derived) :: d

  	class(Base), allocatable :: bb
  	class(Derived), allocatable :: dd

  	call b%add(1)
  	call d%add(2)
  	write(*, *) b%x, d%x

  	allocate(Base :: bb)
  	allocate(Derived :: dd)

  	call f(bb, 10)
  	call f(dd, 20)
  	write(*, *) bb%x, dd%x

  	call f(b, 100)
  	call f(d, 200)
  	write(*, *) b%x, d%x

  end subroutine

end module
"""

open('a.f90','w').write(c)

os.system('ifort a.f90 -warn all -shared -fpic -o a.so')

m = cdll.LoadLibrary('./a.so')

m.a_mp_test_()
