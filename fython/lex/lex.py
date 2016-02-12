from .config import *
from .mark_newlinex import mark_newlinex
from .find_lines import find_lines
from .mark_invisible import mark_invisible
from .translate_fml import translate_fml
from .get_lexer import get_lexer
from .get_lexem import get_lexem
from .mark_unsafe_interpolation_lexem import mark_unsafe_interpolation_lexem
from .mark_opx_from_semix import mark_opx_from_semix
from .mark_eopx import mark_eopx
from .mark_uopx import mark_uopx
from .mark_ropx import mark_ropx

def lex(module):
	mark_newlinex(module)
	find_lines(module)
	mark_invisible(module)

	translate_fml(module)

	if module.verbose.source_with_invisible_and_fml:
		module.verbose_tag('source with invisible and fml')	
		print(module.source_with_invisible_and_fml)
		print()	

	lexer = get_lexer(module)
	
	lexer.input(module.source_with_invisible_and_fml)

	module.lexem = get_lexem(lexer)
	module.lexem_raw = module.lexem + []

	mark_eopx(module)	

	mark_uopx(module)
	
	mark_ropx(module)

	mark_opx_from_semix(module)

	mark_unsafe_interpolation_lexem(module)
	
	if module.verbose.lex:
		module.verbose_tag('module lexem')
		for t in module.lexem:
			print(t.type, repr(t.value.value), t.lineno, t.lexpos)
		print()	