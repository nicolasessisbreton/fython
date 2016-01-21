import os
from ctypes import *

c = """
module a

use ifport, only: signalqq, sig$abort, sig$fpe, sig$ill, sig$int, sig$segv, sig$term, raiseqq

integer :: x = 1


contains

subroutine boom()
	int retcode

	call clear_signal()

	! retcode = raiseqq(sig$abort)
	! retcode = raiseqq(sig$fpe)
	! retcode = raiseqq(sig$ill)
	! retcode = raiseqq(sig$int)
	! retcode = raiseqq(sig$segv)
	! retcode = raiseqq(sig$term)

	x = 1 / 0

	x = 10
end subroutine

subroutine clear_signal()
	int retcode
	retcode = signalqq(sig$abort, abort_handler)
	retcode = signalqq(sig$fpe, fpe_handler)
	write(*, *) 'fpe clear', retcode
	retcode = signalqq(sig$ill, ill_handler)
	retcode = signalqq(sig$int, int_handler)
	retcode = signalqq(sig$segv, segv_handler)
	retcode = signalqq(sig$term, term_handler)
end subroutine

function abort_handler(errorcode) result(r)
	!dir$ attributes c :: abort_handler
	integer(4), intent(in) :: errorcode
	integer(4) :: r
	write(*, *) 'abort'
	r = -1
end function

function fpe_handler(errorcode, floating_error_code) result(r)
	!dir$ attributes c :: fpe_handler
	integer(4), intent(in) :: errorcode
	integer(4), intent(in) :: floating_error_code
	integer(4) :: r
	write(*, *) 'fpe'
	r = -1
end function

function ill_handler(errorcode) result(r)
	!dir$ attributes c :: ill_handler
	integer(4), intent(in) :: errorcode
	integer(4) :: r
	write(*, *) 'ill'
	r = -1
end function

function int_handler(errorcode) result(r)
	!dir$ attributes c :: int_handler
	integer(4), intent(in) :: errorcode
	integer(4) :: r
	write(*, *) 'int'
	r = -1
end function

function segv_handler(errorcode) result(r)
	!dir$ attributes c :: segv_handler
	integer(4), intent(in) :: errorcode
	integer(4) :: r
	write(*, *) 'segv'
	r = -1
end function

function term_handler(errorcode) result(r)
	!dir$ attributes c :: term_handler
	integer(4), intent(in) :: errorcode
	integer(4) :: r
	write(*, *) 'term'
	r = -1
end function

end module
"""
open('a.f90','w').write(c)

os.system('rm a.so')

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

x = c_int.in_dll(m, 'a_mp_x_')
print(x.value)

boom = m.a_mp_boom_
boom()

print(x.value)
