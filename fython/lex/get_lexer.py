from .config import *
from ply.lex import lex as plex
from ..lexem import *

tokens = l.lexems

def t_bofx(t):
	r'<bofx>'
	t.value = ''
	t.value = BofX(t)
	return t

def t_eofx(t):
	r'<eofx>'
	t.value = ''
	t.value = EofX(t)
	return t

def t_linefeedx(t):
	r'<linefeedx\d+>'
	t.lineno = int(t.value[pos_lineno_linefeedx:-1]) - 1 
	t.value = t.lineno
	t.value = LinefeedX(t)
	t.lexer.lineno = t.lineno 
	return t

def t_newlinex(t):
	r'<newlinex>'
	t.value = ''
	t.value = NewlineX(t)
	return t

def t_indentx(t):
	r'<indentx>'
	t.value = ''
	t.value = IndentX(t)
	return t

def t_dedentx(t):
	r'<dedentx>'
	t.value = ''
	t.value = DedentX(t)
	return t

def t_packagex(t):
	r'\|\|'
	if t.lexer.lpackagex_seen:
		t.type = l.rpackagex
		t.lexer.lpackagex_seen = 0
		t.value = RPackageX(t)

	else:
		t.type = l.lpackagex
		t.lexer.lpackagex_seen = 1
		t.value = LPackageX(t)

	return t
	
def t_interpolationx(t):
	r'\|.*?\|'
	t.value = trim(t.value[1:-1])
	t.value = InterpolationX(t)
	return t	

def t_multiline_string_tickx(t):
	r"""'''.*?'''"""
	t.value = trim(t.value[3:-3])
	t.type = l.stringx
	t.value = StringX(t)
	return t 

def t_multiline_string_quotex(t):
	r'''""".*?"""'''
	t.value = trim(t.value[3:-3])
	t.type = l.stringx
	t.value = StringX(t)
	return t 

def t_string_tickx(t):
	r"'(?:[^\\'\n]|\\.)*'"
	t.value = t.value[1:-1]
	t.type = l.stringx
	t.value = StringX(t)
	return t

def t_string_quotex(t):
	r'"(?:[^\\"\n]|\\.)*"'
	t.value = t.value[1:-1]
	t.type = l.stringx
	t.value = StringX(t)
	return t

def t_funx(t):
	r'[\w\$]+\('
	t.value = t.value[:-1]
	t.lexer.group += 1
	t.value = FunX(t)
	return t

def t_slicex(t):
	r'[\w\$]+\['
	t.value = t.value[:-1]
	t.lexer.group += 1
	t.value = SliceX(t)
	return t

def t_numberx(t):
	r'(\d+(\.\d*)?|\.\d+)([eEdD][-+]?\d+)?'
	t.value = NumberX(t)
	return t

def t_namex(t):
	r'[\w\$]+'
	if t.value in ['and', 'or', 'not']:
		t.type = l.opx
		t.value = ' .{:s}. '.format(t.value)
		t.value = OpX(t)

	elif t.value in ['True', 'False', 'true', 'false']:
		t.value = ' .{:s}. '.format(t.value.lower())
		t.value = NumberX(t)

	else:
		t.value = NameX(t)

	return t

def t_iopx(t):
	r'(\+=|-=|\*=|/=|\*\*=|<<=|&=|\^=|[|]=|>>=)' 
	t.value = IOpX(t)
	return t

def t_bopx(t):
	r'(<<|&|\^|[|]|>>)'
	t.value = BOpX(t)
	return t
	
def t_opx_duo(t):
	r'(\*\*|<=|==|!=|>=|=>)'
	if t.value == '!=':
		t.value = '/='	

	t.type = l.opx

	if not t.lexer.group:
		v = t.value
		if v  == '=>':
			t.type = l.iopx
			t.value = IOpX(t)

		else:
			t.value = OpX(t)

	else:
		t.value = OpX(t)

	return t

def t_opx(t):
	r'(\+|\-|\*|/|<|>|:|=)' 
	if not t.lexer.group:
		v = t.value
		if v == '=':
			t.type = l.iopx
			t.value = IOpX(t)

		elif v == ':':
			t.type = l.colonx
			t.value = ColonX(t)
			
		else:
			t.value = OpX(t)

	else:
		t.value = OpX(t)

	return t

def t_dotx(t):
	r'\.+'
	ndx = t.lexer.lexpos - 2
	if ndx < 0:
		t_error(t)

	previous = t.lexer.lexdata[ndx]

	if get_leading_space(previous) or previous in '=(' or t.value.count('.') > 1:
		t.type = l.udotx
		t.value = UDotX(t)
	else:
		t.type = l.bdotx
		t.value = BDotX(t)
	
	return t

def t_commax_semix(t):
	r','
	if t.lexer.group:
		t.type = l.commax
		t.value = CommaX(t)

	else:
		t.type = l.semix
		t.value = SemiX(t)

	return t

def t_lkcax(t):
	r'\]\['
	t.lexer.group += 1
	t.value = LKCaX(t)
	return t

def t_lpcax(t):
	r'\)\['
	t.lexer.group += 1
	t.value = LPCaX(t)
	return t

def t_lparx(t):
	r'\('
	t.lexer.group += 1
	t.value = LParX(t)
	return t

def t_rparx(t):
	r'\)'
	t.lexer.group -= 1
	t.value = RParX(t)
	return t

def t_lketx(t):
	r'\['
	t.lexer.group += 1
	t.value = LKetX(t)
	return t

def t_rketx(t):
	r'\]'
	t.lexer.group -= 1
	t.value = RKetX(t)
	return t

def t_spacex(t):
	r'\s+'

def t_error(t):
	t.lexer.module.throw(
		error = err.syntax_error,
		line = t.lexer.lineno,
		position = t.lexer.lexpos,
		lexem = repr(t.value),
	)

main_lexer = plex(reflags = re.DOTALL )

def get_lexer(module):
	lexer = main_lexer.clone()
	lexer.module = module
	lexer.group = 0
	lexer.lpackagex_seen = 0
	return lexer
