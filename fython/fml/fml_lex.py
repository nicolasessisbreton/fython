from ..config import *
from ply.lex import lex as plex

# lex
tokens = (
	'bofx',
	'eofx',
	'newline',
	'tab',
	'interpolant',
	'lce',
	'rce',
	'string',
)

def t_newline(t):
	r'\n'
	return t

def t_tab(t):
	r'\t'
	return t

def t_interpolant(t):
	r'\{(?P<fmt>[^\{:]*):(?P<arg>[^\}]+)\}'
	t.value = Interpolant(t)
	return t

def t_lce(t):
	r'\{\{'
	t.value = "'{'"
	return t

def t_rce(t):
	r'\}\}'
	t.value = "'}'"
	return t

def t_string(t):
	r'[^\{\}\t\n]+'
	t.value = repr(t.value)
	return t

def t_error(t):
	t.lexer.module.throw(
		err.string_format_error, 
		line = t.lexer.lineno,
		position = t.lexer.lexpos,
		token = repr(t.value),
	)

main_lexer = plex()

class Lexer(Data):

	def __init__(s, module):
		s.module = module
		s.lexer = main_lexer.clone()
		s.lexer.module = module
		s.fmt = []
		s.args = []

		s.star_used = 0	

	def star(s):
		if s.star_used:
			return ''
		else:
			s.star_used = 1
			return '*'
			
	def input(s, source):
		s.lexer.input(source)
		s.tokens = [Bofx()]
		t = s.lexer.token()
		while t:
			s.tokens.append(t)
			t = s.lexer.token()

		s.tokens.append(Eofx())

		if s.module.verbose.fml:
			s.module.verbose_tag('fml: lex')
			for t in s.tokens:
				print(t.type, repr(t.value))

		
	def token(s):
		if s.tokens:
			return s.tokens.pop(0)

	def __add__(s, other):
		s.fmt.append('\"' + other + ',\"')
		return s

	def __truediv__(s, other):
		s.fmt.append('\"' + other + '\"')
		return s

	def __mul__(s, other):
		s.fmt.append(other)
		return s

	def __sub__(s, other):
		s.args.append(other)
		return s

class Bofx:
	type = 'bofx'
	value = ''

	def __repr__(s):
		return 'Bofx()'

class Eofx:
	type = 'eofx'
	value = ''

	def __repr__(s):
		return 'Eofx()'

class Interpolant(Data):
	def __init__(s, t):
		m = t.lexer.lexmatch
		s.fmt = m.group('fmt')
		s.arg = m.group('arg')
		s.value = t.value

	def __repr__(s):
		return "'{:s}' '{:s}'".format(s.fmt, s.arg)