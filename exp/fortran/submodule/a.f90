module a

interface

	module function f(x) result(r)
		use iso_c_binding
		integer :: x
		integer :: r
		integer :: y
	end function

	module function g(x) result(r)
		integer :: x
		integer :: r
		integer :: y
	end function

end interface

end module