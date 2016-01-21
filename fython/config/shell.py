from io import StringIO
from subprocess import Popen, PIPE, STDOUT

def shell(cmd):
	p = Popen(
		cmd, 
		stdout = PIPE, 
		stderr = STDOUT,
		shell = 1,
		universal_newlines = 1,
	)

	out = StringIO()
	for line in iter(p.stdout.readline, ''):
		line = line.rstrip()
		out.write(line)
		out.write('\n')

	out = out.getvalue()

	error = p.poll() != 0

	return out, error
