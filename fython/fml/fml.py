from ..config import *
from .fml_yacc import yacc

fmt_re = re.compile('\{.*:.+\}')

def fml(module, string, to_trim=0):
	if not fmt_re.search(string):
		return string

	elif to_trim:
		string = trim(string[3:-3])

	string = string.lstrip('\'')
	string = string.rstrip('\'')

	fmt, args = yacc(module, string)
	
	fmt = ','.join(fmt)
	
	if fmt.endswith(',"'):
		fmt = fmt[:-2] + '"'

	fmt = '"(",{:s},")"'.format(fmt)

	args = ','.join(args)
	
	r = 'format({:s}) = args({:s})'.format(fmt, args)

	return r
