def open_file(p):
	r = """open( &
	unit = {unit:s}, &
	file = {file:s}, &
	status = 'old', &
	action = 'read' &
)"""

	p(
		r,
		unit = p.unit,
		file = p.path,
	)