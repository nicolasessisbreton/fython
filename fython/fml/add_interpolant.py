from fython.config import *

def add_interpolant(lexer, fmt, arg):
	if fmt == '':
		lexer += 'g0'
		lexer -= arg

	elif fmt == 'v':
		lexer += 'a'
		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)

		lexer /= '(g0,:,'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer += 'a'

		lexer -= "'['"
		lexer -= arg
		lexer -= "']'"

	elif fmt == 'vc':
		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)

		lexer /= '(g0,:,'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer -=  arg

	elif fmt == 'va':
		lexer += 'a'
		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)

		lexer /= '(g0,:,'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer += 'a'

		lexer -= "'array(['"
		lexer -= arg
		lexer -= "'])'"


	else:
		lexer += fmt
		lexer -= arg