
module a

use iso_c_binding

interface
	
	function signal(signum, handler) result(r) bind(c)
		use iso_c_binding
		integer(c_int), value :: signum
		type(c_funptr), value, intent(in) :: handler
		integer(c_int) :: r
	end function

	function setjmp(jmp_buf) result(r) bind(c) 
		use iso_c_binding
		integer(c_int), dimension(100) :: jmp_buf
		integer(c_int) :: r
	end function

	subroutine longjmp(jmp_buf, value) bind(c)
		use iso_c_binding
		integer(c_int), dimension(100) :: jmp_buf
		integer(c_int), value :: value	
	end subroutine

end interface

integer :: x = 1

integer, parameter :: sigint = 2
integer, parameter :: sigill = 4
integer, parameter :: sigabort = 6
integer, parameter :: sigfpe = 8
integer, parameter :: sigsegv = 11
integer, parameter :: sigterm = 15

integer, dimension(100) :: jmp_buf

contains

subroutine boom()
	use iso_c_binding
	integer :: retcode
	type(c_funptr), target :: handler 	
	integer, dimension(2) :: vec

	handler = c_funloc(error_handler)

	retcode = signal(sigint, handler) 
	retcode = signal(sigill, handler) 
	retcode = signal(sigabort, handler)
	retcode = signal(sigfpe, handler)
	retcode = signal(sigsegv, handler)
	retcode = signal(sigterm, handler)

	vec = 10

	retcode = setjmp(jmp_buf)
	write(*, *) 'setjmp', retcode

	if ( val == 0 )then
		write(*, *) 8
		vec(10) = 1
		write(*, *) 9
		x = 1 / 0
	else
		write (*, *) 'smooth exit'
	end if

end subroutine

subroutine error_handler(signum)  bind(c)
	use iso_c_binding
	integer(c_int), intent(in), value :: signum
	write(*, *) 'signum', signum
	call longjmp(jmp_buf, 1)
end subroutine

end module
