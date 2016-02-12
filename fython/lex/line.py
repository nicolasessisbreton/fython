from .config import *

class Line:
	def __init__(s, module, line):
		s.module = module

		if line == '':
			s.is_empty = 1
			s.line = ''
		else:
			ndx = line.rfind('<')
			s.lineno = int(line[ndx+1:])

			s.line = line[:ndx]
			s.line = s.line.rstrip()
			
			s.is_empty = s.line == ''

		if s.is_empty:
			s.has_colon = 0
			s.indent = ''

		else:
			s.has_colon = s.line[-1] == ':'
			s.indent = get_leading_space(line)

	def set_tab_used(s, tab_used):
		s.tab_used = tab_used
		s.level = s.indent.count(tab_used)
		
	def check_for_mixed_indentation(s):
		indent = s.tab_used * s.level
		if indent != s.indent:
			s.throw_mixed_indentation()

	def throw_mixed_indentation(s):
		b = Buffer()
		b += 'previous lines used {:s}'.format(repr(s.tab_used))
		b += 'while this line uses {:s}'.format(repr(s.indent))
		s.throw(err.mixed_indentation, b)

	def throw_cannot_indent_on_first_line(s):
		b = Buffer()
		b += 'indentation is {:s}'.format(repr(s.indent))
		s.throw(err.cannot_indent_on_first_line, b)

	def throw_indentation_without_colon(s):
		b = Buffer()
		b += 'a colon was expected on the previous line'
		b += 'indentation for this line {:s}'.format(repr(s.indent))
		s.throw(err.indentation_without_colon, b)

	def throw_indentation_increased_by_more_than_one_level(s, previous):
		b = Buffer()
		b += 'previous line indent {:d}'.format(previous.count_indent())
		b += 'current line indent level {:d}'.format(s.count_indent())	
		s.throw(err.indentation_increased_by_more_than_one_level, b)

	def count_indent(s):
		return len(s.indent)
		
	def throw_space_tab_mix(s):
		b = Buffer()
		b += 'indentation is {:s}'.format(repr(s.indent))
		s.throw(err.space_tab_mix, b)

	def throw(s, error, msg):
		s.module.throw(
			error,
			line = s.lineno,
			msg = msg,
		)

	def remove_colon(s):
		if s.has_colon:
			s.line = s.line[:-1]