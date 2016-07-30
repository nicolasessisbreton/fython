module m1

interface 
	module subroutine  add(x, y, r)
		real, intent(in) :: x
		real, intent(in) :: y
		real, intent(out) :: r
	end subroutine
end interface

end module