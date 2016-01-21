from fython import *

writer("""
.brent.f90
  module brent
    integer, parameter :: tolerance = 1e-3

  contains

    function root(x) result(r)
      real, dimension(10) :: x
      real :: r
      integer :: i

      r = 0
      
      do i = 1, 10
        r = r + x(i)
      end do

    end function

  end module


.consummer.fy

  import .brent(*)

  real x(10) = 1

  print 'brent says {:root(x)}'
""")

load('.consummer')