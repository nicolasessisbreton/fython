from ..config import *

def open_file(p):
	if p.mode == 'a':
		open_for_append(p)

	elif p.mode == 'w':
		open_for_write(p)
		
	else:
		p.throw(err.unknown_print_mode, mode=p.mode)

def open_for_append(p):
	r = """open( &
	unit = {unit:s}, &
	file = {file:s}, &
	status = 'unknown', &
	action = 'write', &
	position = 'append' &
)"""

	p(
		r,
		unit = p.unit,
		file = p.path,
	)

def open_for_write(p):
	r = """
open( &
	unit = {unit:s}, &
	file = {file:s}, &
	status = 'replace', &
	action='write' &
)
	"""

	p(
		r,
		unit = p.unit,
		file = p.path,
	)