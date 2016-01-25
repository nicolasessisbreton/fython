import os
from ctypes import *
from numpy import *
from time import time

c = """
module a

  integer, parameter :: n = 1e9
  integer, parameter :: m = 1e3

  type :: Solid
    real x(m)
  end type

  type, abstract :: Base
    real x(m)
    contains
    procedure(base_add), deferred, pass(self) :: add
  end type

  type, extends(Base) :: Derived
    contains
    procedure, pass(self) :: add => derived_add
  end type

  abstract interface
    subroutine base_add(self, ndx, value)
      import :: Base
      class(Base), intent(inout) :: self
      integer, intent(in) :: ndx
      real, intent(in) :: value
    end subroutine
  end interface

contains

  subroutine solid_add(self, ndx, value)
    type(Solid), intent(inout) :: self
    integer, intent(in) :: ndx
    real, intent(in) :: value
    self%x(ndx) = value
  end subroutine

  subroutine derived_add(self, ndx, value)
    class(Derived), intent(inout) :: self
    integer, intent(in) :: ndx
    real, intent(in) :: value
    self%x(ndx) = value
  end subroutine

  subroutine test_solid()
    integer i
    integer ndx
    real value
    type(solid) s

    do i = 1, n 
      call random_number(value)
      ndx = m * value
      ndx = max(ndx, 1)
      call solid_add(s, ndx, value)
    end do

  end subroutine

  subroutine test_derived()
    integer i
    integer ndx
    real value
    class(Base), pointer :: s

    allocate(Derived :: s)

    do i = 1, n
      call random_number(value)
      ndx = m * value
      ndx = max(ndx, 1)
      call s%add(ndx, value)
    end do

    deallocate(s)

  end subroutine

end module
"""

open('a.f90','w').write(c)
ifort = 1
gfortran = 1

if ifort:
  print('ifort')
  os.system('ifort a.f90 -shared -fpic -fast -o a.so')

  m = cdll.LoadLibrary('./a.so')

  print('test_solid', '...', end='')
  start = time()
  m.a_mp_test_solid_()
  print(time()-start)

  print('test_derived', '...', end='')
  start = time()
  m.a_mp_test_derived_()
  print(time()-start)

if gfortran:
  print('\ngfortran')

  os.system('gfortran a.f90 -shared -fpic -O3 -o b.so')

  m = cdll.LoadLibrary('./b.so')

  print('test_solid', '...', end='')
  start = time()
  m.__a_MOD_test_solid()
  print(time()-start)

  print('test_derived', '...', end='')
  start = time()
  m.__a_MOD_test_derived()
  print(time()-start)

