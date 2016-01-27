
module a

  integer, parameter :: n = 1e9
  integer, parameter :: m = 1e3

  type :: Solid
    real x(m)
  end type

  type :: Ref
    real x(m)
    contains
    procedure :: add => ref_add
  end type

contains

  subroutine solid_add(self, ndx, value)
    type(Solid), intent(inout) :: self
    integer, intent(in) :: ndx
    real, intent(in) :: value
    self%x(ndx) = value
  end subroutine

  subroutine ref_add(self, ndx, value)
    class(Ref), intent(inout) :: self
    integer, intent(in) :: ndx
    real, intent(in) :: value
    self%x(ndx) = value
  end subroutine

  subroutine test_solid()
    integer i
    integer ndx
    real value
    type(Solid) s

    do i = 1, n 
      call random_number(value)
      ndx = m * value
      ndx = max(ndx, 1)
      call solid_add(s, ndx, value)
    end do

  end subroutine

  subroutine test_ref()
    integer i
    integer ndx
    real value
    type(Ref) s

    do i = 1, n
      call random_number(value)
      ndx = m * value
      ndx = max(ndx, 1)
      call s%add(ndx, value)
    end do

  end subroutine

end module
