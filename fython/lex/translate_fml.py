from .config import *
from ply.lex import lex as plex
from fython.fml import *

tokens = (
	'string',
	'code',
)

def t_interpolationx(t):
	r'\|.*?\|'
	t.type = 'code'
	return t	

def t_multiline_string_tickx(t):
	r"""'''.*?'''"""
	t.type = 'string'
	t.value = fml(t.lexer.module, t.value)
	return t 

def t_multiline_string_quotex(t):
	r'''""".*?"""'''
	t.type = 'string'
	t.value = fml(t.lexer.module, t.value)
	return t 

def t_string_tickx(t):
	r"'(?:[^\\'\n]|\\.)*'"
	t.type = 'string'
	t.value = fml(t.lexer.module, t.value)
	return t 

def t_string_quotex(t):
	r'"(?:[^\\"\n]|\\.)*"'
	t.type = 'string'
	t.value = fml(t.lexer.module, t.value)
	return t 

def t_code(t):
	r"""[^'"\|]+"""
	return t

def t_error(t):
	t.lexer.module.throw(
		error = err.fml_error,
		line = t.lexer.lineno,
		position = t.lexer.lexpos,
		lexem = repr(t.value),
	)

main_lexer = plex(reflags = re.DOTALL )

def translate_fml(module):
	lexer = main_lexer.clone()
	lexer.module = module
	lexer.input(module.source_with_invisible)

	r = ''
	t = lexer.token()
	while t:
		r += t.value
		t = lexer.token()

	module.source_with_invisible_and_fml = r