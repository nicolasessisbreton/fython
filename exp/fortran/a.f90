
module a
	
	type AA
		real x(10)
	end type

	type(AA) y(10)
contains

subroutine f() 
	write(*, *) y(1)%x(1)

end subroutine

end module
