module m1

contains

subroutine  cube_mean(x, y, z, r) 
	real, intent(in) :: x
	real, intent(in) :: y
	real, intent(in) :: z
	real, intent(out) :: r

	r=x+y+z
	r = r / (3)
	r = r * (3)


end subroutine

end module