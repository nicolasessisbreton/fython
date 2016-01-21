from ..config import *
from .fml_yacc import yacc

fmt_re = re.compile('\{.*:.+\}')

def fml(module, string):
	if not fmt_re.search(string):
		return string

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



