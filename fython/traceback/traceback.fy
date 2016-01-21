import iso_c_binding(*)

interface:
	def iso(c) signal:
		int(c_int) value in signum
		c_funptr value in handler
		int(c_int) res r

	def iso(c) setjmp:
		int(c_int) dimension(100) arg jmp_buf
		int(c_int) res r

	def iso(c) longjmp:
		int(c_int) dimension(100) arg jmp_buf
		int(c_int) value arg value	


int(c_int) cons sigint = 2
int(c_int) cons sigill = 4
int(c_int) cons sigabort = 6
int(c_int) cons sigfpe = 8
int(c_int) cons sigsegv = 11
int(c_int) cons sigterm = 15

int cons max_depth = 300
int cons dotted_length = 300

char(dotted_length) dimension(max_depth) dotted
int dimension(max_depth) lineno

int ndx # frame index

char(300) last_error

int error_occured

int dimension(100) jmp_buf

int verbose = 0

def iso(c) error_handler:
	int(c_int) in value signum

	if signum == sigint:
		last_error = 'sigint: interruption'
	elif signum == sigill:
		last_error = 'sigill: invalid instruction'
	elif signum == sigabort:
		last_error = 'sigabort: abnormal termination'
	elif signum == sigfpe:
		last_error = 'sigfpe: floating point error'
	elif signum == sigsegv:
		last_error = 'sigsegv: segmentation fault'
	elif signum == sigterm:
		last_error = 'sigterm: termination'
	else:
		print unit(last_error) 'unknown error, signum = {:signum}'

	error_occured = 1

	longjmp(jmp_buf, 1)

def reset:
	int retcode
	c_funptr target handler

	ndx = 0

	error_occured = 0

	handler = c_funloc(error_handler)

	retcode = signal(sigint, handler) 
	retcode = signal(sigill, handler) 
	retcode = signal(sigabort, handler)
	retcode = signal(sigfpe, handler)
	retcode = signal(sigsegv, handler)
	retcode = signal(sigterm, handler)

def init_frame:
	char(*) in d
	if error_occured == 0:
		ndx += 1
		dotted[ndx] = d

def del_frame:
	if error_occured == 0:
		ndx -= 1

def advance_line:
	int in l
	int	res r
	r = setjmp(jmp_buf)
	
	if error_occured == 0:
		lineno[ndx] = l
		if verbose == 1:
			print '{:trim(dotted[ndx])} {:l}'
		r = 1
		
	else:
		r = 0

def int_to_char:
	int in x
	char(20) res r
	print r '{:x}'