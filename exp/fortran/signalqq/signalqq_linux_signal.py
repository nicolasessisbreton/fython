c = """
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

	handler = c_funloc(error_handler)

	retcode = signal(sigint, handler) 
	retcode = signal(sigill, handler) 
	retcode = signal(sigabort, handler)
	retcode = signal(sigfpe, handler)
	retcode = signal(sigsegv, handler)
	retcode = signal(sigterm, handler)

	val = setjmp(jmp_buf)

	if ( val == 0 )then
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
"""

import os
from ctypes import *

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


"""
from ifport
INTEGER(4), PARAMETER :: SIG$ERR   = -1
INTEGER(4), PARAMETER :: SIG$INT   =  2
INTEGER(4), PARAMETER :: SIG$ILL   =  4
INTEGER(4), PARAMETER :: SIG$FPE   =  8
INTEGER(4), PARAMETER :: SIG$SEGV  = 11
INTEGER(4), PARAMETER :: SIG$TERM  = 15
INTEGER(4), PARAMETER :: SIG$USR1  = 16
INTEGER(4), PARAMETER :: SIG$USR2  = 17
INTEGER(4), PARAMETER :: SIG$USR3  = 20
INTEGER(4), PARAMETER :: SIG$BREAK = 21
INTEGER(4), PARAMETER :: SIG$ABORT = 22
INTEGER(4), PARAMETER :: SIG$NSIG  = 23

from signum.h

/* Signals.  */
#define	SIGHUP		1	/* Hangup (POSIX).  */
#define	SIGINT		2	/* Interrupt (ANSI).  */
#define	SIGQUIT		3	/* Quit (POSIX).  */
#define	SIGILL		4	/* Illegal instruction (ANSI).  */
#define	SIGTRAP		5	/* Trace trap (POSIX).  */
#define	SIGABRT		6	/* Abort (ANSI).  */
#define	SIGIOT		6	/* IOT trap (4.2 BSD).  */
#define	SIGBUS		7	/* BUS error (4.2 BSD).  */
#define	SIGFPE		8	/* Floating-point exception (ANSI).  */
#define	SIGKILL		9	/* Kill, unblockable (POSIX).  */
#define	SIGUSR1		10	/* User-defined signal 1 (POSIX).  */
#define	SIGSEGV		11	/* Segmentation violation (ANSI).  */
#define	SIGUSR2		12	/* User-defined signal 2 (POSIX).  */
#define	SIGPIPE		13	/* Broken pipe (POSIX).  */
#define	SIGALRM		14	/* Alarm clock (POSIX).  */
#define	SIGTERM		15	/* Termination (ANSI).  */
#define	SIGSTKFLT	16	/* Stack fault.  */
#define	SIGCLD		SIGCHLD	/* Same as SIGCHLD (System V).  */
#define	SIGCHLD		17	/* Child status has changed (POSIX).  */
#define	SIGCONT		18	/* Continue (POSIX).  */
#define	SIGSTOP		19	/* Stop, unblockable (POSIX).  */
#define	SIGTSTP		20	/* Keyboard stop (POSIX).  */
#define	SIGTTIN		21	/* Background read from tty (POSIX).  */
#define	SIGTTOU		22	/* Background write to tty (POSIX).  */
#define	SIGURG		23	/* Urgent condition on socket (4.2 BSD).  */
#define	SIGXCPU		24	/* CPU limit exceeded (4.2 BSD).  */
#define	SIGXFSZ		25	/* File size limit exceeded (4.2 BSD).  */
#define	SIGVTALRM	26	/* Virtual alarm clock (4.2 BSD).  */
#define	SIGPROF		27	/* Profiling alarm clock (4.2 BSD).  */
#define	SIGWINCH	28	/* Window size change (4.3 BSD, Sun).  */
#define	SIGPOLL		SIGIO	/* Pollable event occurred (System V).  */
#define	SIGIO		29	/* I/O now possible (4.2 BSD).  */
#define	SIGPWR		30	/* Power failure restart (System V).  */
#define SIGSYS		31	/* Bad system call.  */
#define SIGUNUSED	31

"""