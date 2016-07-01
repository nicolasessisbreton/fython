s = r"""
.a.fy
	integer: x=8, var_name_without_dot=10, any_var_name=10 
	integer: float int vector(10) vector_content(10) 
	char(10): variable_name='./file', string = 'abcdef'

	# basic
	print 'x {:x}'

	# dotted
	print .file 'x1 {:x}'
	print url(.file) 'x2 {:x}'

	# in variable or unit
	open(10, file=variable_name)
	print 10 'x3 {:x}' # number
	print var_name_without_dot 'x4 {:x}'
	print unit(any_var_name) 'x5 {:x}'
	close(10)

	# path
	print './out' 'x6'
	print path('./out') 'x7'
	print path(variable_name) 'x8'

	# suite
	print:
		'x9'
		'y10'

	# multiline
	# format are fortran format plus some addition
	# 	see fython.format_mini_language.format_mini_language_desc
	print '''
	multiline:

	{f:float} 
	{i:int} 
	{v:vector} 
	{vc:vector_content}
	{a:string}
	'''

	# xip
	xip 'printed only in debug mode'
"""

from fython.test import *

writer(s)

w = load('.a', force=1, release=1, verbose=0, run_main=0)
# print(open(w.module.url.fortran_path, 'r').read())
