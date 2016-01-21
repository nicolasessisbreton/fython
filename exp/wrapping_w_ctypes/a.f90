module a

use iso_c_binding

integer, bind(c) :: global = 88

contains

function add(x) bind(c) result(r)
	real(c_float) :: x
	real(c_float) :: r
	r =  x + 1
end function

function tot(x, n) bind(c) result(r)
	integer(c_int) :: n
	real(c_float), dimension(n) :: x
	real(c_float) :: r
	r =  sum(x)
end function

subroutine mod(x) bind(c) 
	real(c_float), dimension(3), intent(out) :: x
	x = 1
end subroutine

subroutine s(x, n) bind(c)
	character(1, c_char), dimension(3) :: x
	write(x, '(i0)') 9
end subroutine

subroutine svec(x) bind(c)
	character(1, c_char), dimension(4, 3) :: x
	character(3), dimension(4) :: y 
	! transfer
	y(1)(1:1) = x(1, 1)
	y(1)(2:2) = x(2, 1)
	y(1)(3:3) = x(3, 1)

	!copy
	x(1, 3) = y(1)(1:1)
	x(2, 3) = y(1)(2:2)
	x(3, 3) = y(1)(3:3)

end subroutine

subroutine err(x) bind(c)
	real(c_float) x
	real y
	x = 10
	y = 1 / 0
end subroutine

end module