from ..config import *
from tabulate import tabulate

def stack_trace(last_error, ndx, dotted, lineno):
	last_error = last_error.decode('utf-8').strip()
	n = ndx
	name = []
	line = []
	for i in range(n):
		name.append(dotted[i].decode('utf-8').strip())
		line.append(str(lineno[i]))

	name = list(reversed(name))
	line = list(reversed(line))
	module = []
	function = []
	for n in name:
		m, f = n.split(':')
		module.append(m)
		function.append(f)

	b = Buffer()

	b(
		"""
fython {error:s}

module {module:s}
function {function:s}
line {line:s}

stack trace (lineno function module) (most recent first)
		""",
		error = last_error,
		module = module[0],
		function = function[0],
		line = line[0],
	)

	b += tabulate(
		zip(line, function, module),
		tablefmt = 'plain',
	)
	
	raise Exception(b.r)