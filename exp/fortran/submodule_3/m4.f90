module m4
use m2

contains

subroutine  call_std_deviation(x, y, z, r) 
	real, intent(in) :: x, y, z
	real, intent(out) :: r
	call std(x, y, z, r)

end subroutine


end module