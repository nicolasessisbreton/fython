import re
from .config import *
from ply.lex import lex as plex
from ply.yacc import yacc as pyacc
from .unbalanced_parenthesis_locator import find_unbalanced_parenthesis

newline_re = re.compile('\n+')

# newlinex marking
tokens = (
	'bofx',
	'eofx',

	'lpar',
	'rpar',
	'lket',
	'rket',

	'newline',

	'code',
)

def t_bofx(t):
	r'<bofx>'
	t.value = ''
	return t

def t_eofx(t):
	r'<eofx>'
	t.value = ''
	return t

def t_packagex(t):
	r'\|\|.*?\|\|'
	t.type = 'code'
	t.lexer.lineno += t.value.count('\n')
	t.value = t.value.replace('\t', '')
	t.value = t.value.replace(' ', '')
	t.value = newline_re.sub(',', t.value) 
	t.value = t.value.replace(',||', '||')
	t.value = t.value.replace('||,', '||')
	return t	

def t_interpolationx(t):
	r'\|.*?\|'
	t.lexer.lineno += t.value.count('\n')
	t.type = 'code'
	return t	

def t_multiline_comment(t):
	r'\#\#.*?\#\#'
	t.lexer.lineno += t.value.count('\n')
	t.value = ''
	t.type = 'code'
	return t	

def t_singleline_comment(t):
	r'\#.*?\n'
	t.lexer.lexpos -= 1
	t.value = ''
	t.type = 'code'
	return t

def t_multiline_string_tick(t):
	r"""'''.*?'''"""
	t.lexer.lineno += t.value.count('\n')
	t.type = 'code'
	return t 

def t_multiline_string_quote(t):
	r'''""".*?"""'''
	t.lexer.lineno += t.value.count('\n')
	t.type = 'code'
	return t 

def t_string_tick(t):
	r"'(?:[^\\'\n]|\\.)*'"
	t.type = 'code'
	return t

def t_string_quote(t):
	r'"(?:[^\\"\n]|\\.)*"'
	t.type = 'code'
	return t

def t_lpar(t):
	r'\('
	t.lexer.group += 1
	return t

def t_rpar(t):
	r'\)'
	t.lexer.group -= 1
	return t

def t_lket(t):
	r'\['
	t.lexer.group += 1
	return t

def t_rket(t):
	r'\]'
	t.lexer.group -= 1
	return t

def t_newline(t):
	r'\n'
	t.lexer.lineno += 1

	if t.lexer.group:
		t.type = 'code'
	else:
		t.value = newlinex_mark.format(t.lexer.lineno)

	return t

def t_code(t):
	r'[^\'"\#\(\[\)\]\n\|]+'
	return t

def t_error(t):
	t.lexer.module.throw(
		err.mark_newlinex_lexing_error, 
		line = t.lexer.lineno,
		lexem = repr(t),
	)

main_lexer = plex(reflags=re.DOTALL)

# group check
def p_bofx(p):
	"""
	source	:	bofx
	"""
	p[0] = p[1]

def p_source(p):
	"""
	source 	: 	source element
	"""
	p[0] = p[1] + p[2]

def p_source_unary(p):
	"""
	element : 	code
			| 	newline
			| 	par
			|	ket
	"""	
	p[0] = p[1]

def p_eofx(p):
	"""
	source	:	source eofx	
	"""
	p[0] = p[1] + p[2]	
	return p[0]

def p_parR(p):
	"""
	parR 	: 	lpar
	"""
	p[0] = p[1]

def p_par_cont(p):
	"""
	parR 	: 	parR element
	"""
	p[0] = p[1] + p[2]	

def p_par(p):
	"""
	par : parR rpar
	"""
	p[0] = p[1] + p[2]

def p_ketR(p):
	"""
	ketR 	: 	lket
	"""
	p[0] = p[1]

def p_ket_cont(p):
	"""
	ketR 	: 	ketR element
	"""
	p[0] = p[1] + p[2]	

def p_ket(p):
	"""
	ket : ketR rket
	"""
	p[0] = p[1] + p[2]

def p_error(p):
	p.lexer.module.throw(
		error = err.unbalanced_parenthesis,
		msg = find_unbalanced_parenthesis(p.lexer.module.source),
	)

parser = pyacc(tabmodule = 'mark_newlinex_parsetab')

def mark_newlinex(module):
	lexer = main_lexer.clone()
	lexer.module = module
	lexer.group = 0
	source = '<bofx>' + module.source + '\n<eofx>' # make sure eof is smooth

	if module.verbose.mark_newlinex:
		module.verbose_tag('mark newlinex: lex')
		lexer.input(source)
		t = lexer.token()
		while t:
			print(t.type, repr(t.value), t.lineno, t.lexpos)
			t = lexer.token()
		print()	

	if module.verbose.mark_newlinex:
		module.verbose_tag('mark newlinex: yacc')

	r = parser.parse(
		source, 
		lexer = lexer, 
		debug = module.verbose.mark_newlinex,
	)

	module.source_marked = r
	
	if module.verbose.mark_newlinex:
		module.verbose_tag('mark newlinex: source marked')
		print(module.source_marked)