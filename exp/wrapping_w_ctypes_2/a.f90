module a

integer, bind(c) :: global = 88
integer, dimension(2), bind(c) :: global_vec = [10, 20]
real :: global_not_bind = 1

contains

function add(x) bind(c) result(r)
	real :: x
	real :: r
	r =  x + 1
	global = x
	global_vec(2) = x
end function

function add_wo_bind(x)  result(r)
	real :: x
	real :: r
	r =  x + 1
end function

function tot(x, n) bind(c) result(r)
	integer :: n
	real, dimension(n) :: x
	real :: r
	r =  sum(x)
end function

subroutine mod(x) bind(c) 
	real, dimension(3), intent(out) :: x
	x = 1
end subroutine

subroutine s(x, n) bind(c)
	character(1), dimension(3) :: x
	write(x, '(i0)') 9
end subroutine

subroutine s_wo_bind(x, n) 
	character(30) :: x
	write(*, *) 9, x
end subroutine

subroutine svec(x) bind(c)
	character(1), dimension(4, 3) :: x
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

subroutine svec_wo_bind(x) 
	character(3), dimension(4) :: x
	write(*, *) x(1), 1
	write(*, *) x(2), 2
	write(*, *) x(3), 3
	write(*, *) x(4), 4
end subroutine

subroutine err(x) bind(c)
	real x
	real y
	x = 10
	y = 1 / 0
end subroutine

end module