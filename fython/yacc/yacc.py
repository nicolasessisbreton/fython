from ply.yacc import yacc as pyacc
from ..config import *
from ..code import *
from ..symbol import *

tokens = l.lexems

def p_code_bofx(p):
	"""
	code	:	bofx
	"""
	p[0] = Code(p[1])

def p_code_friendcod(p):
	"""
	code	:	code linecod
	"""
	p[0] = p[1] + p[2]

def p_eofx(p):
	"""
	code	:	code eofx
	"""
	p[0] = p[1] + p[2] 
	return p[0]

def p_linecod(p):
	"""
	linecod :	linecodR childcod
			|	linecodR enumbol
			|	linecodR ibol
			|	linecodR newlinex	
	"""
	p[0] = p[1] & p[2]

def p_linecodR_init(p):
	"""
	linecodR	:	linefeedx
	"""
	p[0] = LineCod(p[1])

def p_linecodR_cond(p):
	"""
	linecodR	:	linecodR element
	"""
	p[0] = p[1] & p[2]

def p_childcod(p):
	"""
	childcod	:	childcodR dedentx
	"""
	p[0] = p[1] + p[2]

def p_childcod_init(p):
	"""
	childcodR	:	indentx
	"""
	p[0] = ChildCod(p[1])

def p_childcod_cond(p):
	"""
	childcodR	:	childcodR linecod
	"""
	p[0] = p[1] + p[2]

def p_element(p):
	"""
	element	:	symbol
			|	lexem
	"""
	p[0] = p[1]

def p_symbol(p):
	"""
	symbol 	:	dotbol
			|	funbol
			|	slicebol
			|	parbol
			|	ketbol
			|	opbol
			|	packagebol
			|	semibol
			|	bitbol
	"""
	p[0] = p[1]

def p_enumbol(p):
	"""
	enumbol	:	enumbolR newlinex
	"""
	p[0] = p[1] & p[2]
	
def p_enumbolR_init(p):
	"""
	enumbolR	:	colonx
	"""
	p[0] = EnumBol(p[1])

def p_enumbolR_cont(p):
	"""
	enumbolR	:	enumbolR element
	"""
	p[0] = p[1] & p[2]	
	
def p_ibol(p):
	"""
	ibol 	:	ibolR newlinex
	"""
	p[0] = p[1] & p[2]

def p_ibolR_init(p):
	"""
	ibolR	:	element iopx
	"""
	p[0] = IBol(p[1], p[2])

def p_ibolR_element(p):
	"""
	ibolR	:	ibolR element
	"""
	p[0] = p[1] & p[2]

def p_dotbol_unary(p):
	"""
	dotbol	:	udotx element
	"""
	p[0] = DotBol(p[1], p[2])

def p_dotbol_binary(p):
	"""
	dotbol	:	element bdotx element
	"""
	p[0] = DotBol(p[1], p[2], p[3])

def p_funbol(p):
	"""
	funbol	:	funbolR rparx
			|	funbolR rketx
	"""
	p[0] = p[1] & p[2]

def p_funbolR_init(p):
	"""
	funbolR : 	funx
	"""
	p[0] = FunBol(p[1])

def p_funbolR_cont(p):
	"""
	funbolR		:	funbolR element
	"""
	p[0] = p[1] & p[2]

def p_slicebol(p):
	"""
	slicebol	:	slicebolR rketx
	"""
	p[0] = p[1] & p[2]

def p_slicebolR_init(p):
	"""
	slicebolR 	: 	slicex
	"""
	p[0] = SliceBol(p[1])

def p_slicebolR_cont(p):
	"""
	slicebolR	:	slicebolR element
	"""
	p[0] = p[1] & p[2]


def p_parbol(p):
	"""
	parbol	:	parbolR rparx
	"""
	p[0] = p[1] & p[2]

def p_parbolR_init(p):
	"""
	parbolR	:	lparx
	"""
	p[0] = ParBol(p[1])

def p_parbolR_cont(p):
	"""
	parbolR	:	parbolR element
	"""
	p[0] = p[1] & p[2]
	
def p_ketbol(p):
	"""
	ketbol	:	ketbolR rketx
	"""
	p[0] = p[1] & p[2]

def p_ketbolR_init(p):
	"""
	ketbolR	:	lketx
	"""
	p[0] = KetBol(p[1])

def p_ketbolR_cont(p):
	"""
	ketbolR	:	ketbolR element
	"""
	p[0] = p[1] & p[2]

def p_opbol_unary(p):
	"""
	opbol	:	uopx element
			|	element ropx
	"""
	p[0] = OpBol(p[1], p[2])

def p_opbol_binary(p):
	"""
	opbol	:	element opx element
	"""
	p[0] = OpBol(p[1], p[2], p[3])

def p_packagebol_init(p):
	"""
	packagebolR	:	lpackagex
	"""
	p[0] = PackageBol(p[1])

def p_packagebol_cont(p):
	"""
	packagebolR	:	packagebolR element
	"""
	p[0] = p[1] & p[2]

def p_packagebol(p):
	"""
	packagebol	:	packagebolR rpackagex
	"""
	p[0] = p[1] & p[2]

def p_semibol(p):
	"""
	semibol	:	element semix element
	"""
	p[0] = SemiBol(p[1], p[2], p[3])

def p_bitbol(p):
	"""
	bitbol 	: 	element bopx element
	"""
	p[0] = BitBol(p[1], p[2], p[3])
			
def p_lexem(p):
	"""
	lexem	:	stringx
			|	namex
			|	numberx
			|	opx
			|	commax
			|	lkcax
			|	lpcax
			|	eopx
	"""
	p[0] = p[1]

precedence = (
	('left', l.semix,),
	('left' , l.opx,),
	('left', l.bdotx,),
	('right', l.udotx,), 
)

def p_error(p):
	p.value.throw(err.syntax_error, lexem=repr(p.value.value))

parser = pyacc(tabmodule = 'yacc_parsetab')

def yacc(module):
	if module.verbose.yacc:
		module.verbose_tag('module yacc')
		
	code = parser.parse(
		module.source,
		lexer = module,
		debug = module.verbose.yacc,
	)

	module.code = code.linecod