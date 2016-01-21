module mx

interface

module subroutine  std_deviation(x, y, z, r) 
	real, intent(in) :: x, y, z
	real, intent(out) :: r
	real :: u


end subroutine


end interface

contains

module procedure std_deviation
	call cube_mean(x, y, z, u)
	r=x-u

end procedure


end module