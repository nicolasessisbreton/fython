
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
    class(Base), allocatable :: s

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
