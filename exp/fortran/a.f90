
module a

contains
	subroutine f(x, y)
		real :: x, y
	end subroutine

	subroutine g()
		call f(y=1., x=x)
	end subroutine
end module
