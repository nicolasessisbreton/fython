import os
from ctypes import *

c = """
module bc0eb009f9
use ifport, only: signalqq=>signal, sig$abort=>sigabort, sig$fpe=>sigfpe, sig$ill=>sigill, sig$segv=>sigsegv, sig$term=>sigterm, fpe$invalid=>fpe_invalid, fpe$denormal=>fpe_denormal, fpe$zerodivide=>fpe_zerodivide, fpe$overflow=>fpe_overflow, fpe$underflow=>fpe_underflow, fpe$inexact=>fpe_inexact, fpe$unemulated=>fpe_unemulated, fpe$sqrtneg=>fpe_sqrtneg, fpe$stackoverflow=>fpe_stackoverflow, fpe$stackunderflow=>fpe_stackunderflow, fpe$explicitgen=>fpe_explicitgen

integer, parameter :: max_depth=300
integer, parameter :: dotted_length=300

character(dotted_length), dimension(max_depth) :: dotted
integer, dimension(max_depth) :: lineno

integer :: ndx

character(300) :: last_error

private :: signal,sigabort,sigfpe,sigill,sigint,sigsegv,sigterm,fpe_invalid,fpe_denormal,fpe_zerodivide,fpe_overflow,fpe_underflow,fpe_inexact,fpe_unemulated,fpe_sqrtneg,fpe_stackoverflow,fpe_stackunderflow,fpe_explicitgen,max_depth,dotted_length,dotted,lineno,ndx,last_error,clear_signal,abort_handler,fpe_handler,ill_handler,int_handler,segv_handler,term_handler,reset
! signal
contains

subroutine  clear_signal() 
	integer :: retcode
	retcode=signalqq(sigabort, abort_handler)
	retcode=signal(sigfpe, fpe_handler)
	retcode=signal(sigill, ill_handler)
	retcode=signal(sigint, int_handler)
	retcode=signal(sigsegv, segv_handler)
	retcode=signal(sigterm, term_handler)

end subroutine
function  abort_handler(error_code)  result(r)
	!dir$ attributes c :: abort_handler

	integer, intent(in) :: error_code
	integer :: r
	last_error='sigabort: abnormal termination'
	r=-1

end function
function  fpe_handler(error_code, floating_error_code)  result(r)
	!dir$ attributes c :: fpe_handler

	integer, intent(in) :: error_code
	integer, intent(in) :: floating_error_code
	integer :: r

	if (floating_error_code==fpe_invalid) then 
	 		last_error='sigfpe: floating point error, fpe_invalid' 
	else if (floating_error_code==fpe_denormal) then 
	 		last_error='sigfpe: floating point error, fpe_denormal' 
	else if (floating_error_code==fpe_zerodivide) then 
	 		last_error='sigfpe: floating point error, fpe_zerodivide' 
	else if (floating_error_code==fpe_overflow) then 
	 		last_error='sigfpe: floating point error, fpe_overflow' 
	else if (floating_error_code==fpe_underflow) then 
	 		last_error='sigfpe: floating point error, fpe_underflow' 
	else if (floating_error_code==fpe_inexact) then 
	 		last_error='sigfpe: floating point error, fpe_inexact' 
	else if (floating_error_code==fpe_unemulated) then 
	 		last_error='sigfpe: floating point error, fpe_unemulated' 
	else if (floating_error_code==fpe_sqrtneg) then 
	 		last_error='sigfpe: floating point error, fpe_sqrtneg' 
	else if (floating_error_code==fpe_stackoverflow) then 
	 		last_error='sigfpe: floating point error, fpe_stackoverflow' 
	else if (floating_error_code==fpe_stackunderflow) then 
	 		last_error='sigfpe: floating point error, fpe_stackunderflow' 
	else if (floating_error_code==fpe_explicitgen) then 
	 		last_error='sigfpe: floating point error, fpe_explicitgen' 
	else 
	 		last_error='sigfpe: floating point error, fpe_explicitgen' 
	end if

	r=-1

end function
function  ill_handler(error_code)  result(r)
	!dir$ attributes c :: ill_handler

	integer, intent(in) :: error_code
	integer :: r
	last_error='sigill: illegal instruction'
	r=-1

end function
function  int_handler(error_code)  result(r)
	!dir$ attributes c :: int_handler

	integer, intent(in) :: error_code
	integer :: r
	last_error='sigint: interruption signal'
	r=-1

end function
function  segv_handler(error_code)  result(r)
	!dir$ attributes c :: segv_handler

	integer, intent(in) :: error_code
	integer :: r
	last_error='sissegv: segmentation fault'
	r=-1

end function
function  term_handler(error_code)  result(r)
	!dir$ attributes c :: term_handler

	integer, intent(in) :: error_code
	integer :: r
	last_error='sigterm: termination request'
	r=-1

end function
! pywrapper utils
subroutine  reset() 
	ndx=0

end subroutine
! traceback effecter
subroutine  fytbk_init_frame(d) 
	character(*), intent(in) :: d
	ndx = ndx + (1)
	dotted(ndx)=d

end subroutine
subroutine  fytbk_del_frame() 
	ndx = ndx - (1)

end subroutine
subroutine  fytbk_advance_line(l) 
	integer, intent(in) :: l
	lineno(ndx)=l

end subroutine


end module"""
open('a.f90','w').write(c)

os.system('ifort a.f90 -shared -fpic -o a.so')

os.system('nm -D a.so')

m = cdll.LoadLibrary('./a.so')

x = c_int.in_dll(m, 'a_mp_x_')
print(x.value)

boom = m.a_mp_boom_
boom()
