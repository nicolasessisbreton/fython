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

	elif fmt == 'jn':
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer /= '('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer += ')'

		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(arg)
		lexer -= 'achar(34)'
		lexer -= '":"'
		lexer -= arg

	elif fmt == 'j':
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer /= '('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer += ')'

		lexer -= '","'
		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(arg)
		lexer -= 'achar(34)'
		lexer -= '":"'
		lexer -= arg


	elif fmt == 'jv':
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)
		lexer /= '(('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= '),'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer += 'tl2,a'

		lexer -= '","'
		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(arg)
		lexer -= 'achar(34)'
		lexer -= '": ["'
		lexer -= arg
		lexer -= '"]"'


	elif fmt == 'jvn':
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)
		lexer /= '(('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= '),'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer += 'tl2,a'

		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(arg)
		lexer -= 'achar(34)'
		lexer -= '": ["'
		lexer -= arg
		lexer -= '"]"'

	elif fmt.startswith('jn_'):
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer /= '('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer += ')'

		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(fmt[3:])
		lexer -= 'achar(34)'
		lexer -= '":"'
		lexer -= arg

	elif fmt.startswith('j_'):
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer /= '('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer += ')'

		lexer -= '","'
		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(fmt[2:])
		lexer -= 'achar(34)'
		lexer -= '":"'
		lexer -= arg

	elif fmt.startswith('jv_'):
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)
		lexer /= '(('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= '),'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer += 'tl2,a'

		lexer -= '","'
		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(fmt[3:])
		lexer -= 'achar(34)'
		lexer -= '": ["'
		lexer -= arg
		lexer -= '"]"'

	elif fmt.startswith('jvn_'):
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'
		lexer += 'a'

		lexer *= 'trim({:s}(size({:s})))'.format(fytbk.int_to_char_tag, arg)
		lexer /= '(('
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= ',g0,'
		lexer *= 'achar(39)'
		lexer *= 'achar(34)'
		lexer *= 'achar(39)'
		lexer /= '),'
		lexer *= 'achar(34)'
		lexer /= ', '
		lexer *= 'achar(34)'
		lexer += ')'

		lexer += 'tl2,a'

		lexer -= 'achar(34)'
		lexer -= '"{:s}"'.format(fmt[4:])
		lexer -= 'achar(34)'
		lexer -= '": ["'
		lexer -= arg
		lexer -= '"]"'

	else:
		lexer += fmt
		lexer -= arg