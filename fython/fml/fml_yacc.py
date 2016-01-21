from ply.yacc import yacc as pyacc
from .fml_lex import tokens, Lexer
from .add_interpolant import add_interpolant

def p_bofx(p):
	"""
	start 	: 	bofx
			|	start eofx
			|	start code
	"""
	pass # nothing to do

def p_newline(p):
	"""
	code 	: 	newline 
	"""
	p.lexer += 'a'
	p.lexer -= 'char(10)'
			
def p_tab(p):
	"""
	code 	: 	tab
	"""
	p.lexer += 'a'
	p.lexer -= 'char(9)'

def p_string(p):
	"""
	code 	: 	string
	"""
	p.lexer += 'a'
	p.lexer -= p[1]
	
def p_lce(p):
	"""
	code 	: 	lce
	"""
	p.lexer += 'a'
	p.lexer -= p[1]

def p_rce(p):
	"""
	code 	: 	rce
	"""
	p.lexer += 'a'
	p.lexer -= p[1]

def p_interpolant(p):
	"""
	code 	: 	interpolant
	"""
	add_interpolant(
		lexer = p.lexer, 
		fmt = p[1].fmt, 
		arg = p[1].arg,
	)

def p_error(p):
	p.lexer.module.throw(
		err.string_format_error, 
		line = p.lineno,
		position = p.lexpos,
	)

parser = pyacc(tabmodule = 'fml_parsetab')

def yacc(module, source):
	lexer = Lexer(module)

	if module.verbose.fml:
		module.verbose_tag('fml: yacc')
		
	parser.parse(
		source, 
		lexer = lexer,
		debug = module.verbose.fml,
	)

	return lexer.fmt, lexer.args
	
	
	
	
	
	



	