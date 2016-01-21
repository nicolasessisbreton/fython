from .config import *
from .line import Line

def find_lines(module):
	source_lines = module.source_marked.split(newlinex)
	n = len(source_lines)
	lines = []

	for line in source_lines:
		x = Line(module, line)
		lines.append(x)

	# find tabbing method:
	tab_used = '\t'
	for i in range(1, n):
		if lines[i-1].has_colon:
			space = lines[i].indent
			tab_here = space.count('\t')
			space_here = space.count(' ')
			if tab_here != 0 and space_here !=0:
				lines[i].throw_space_tab_mix()
			else:
				tab_used = space
				break

	# no indent on first line
	line = lines[0]
	line.set_tab_used(tab_used)
	line.check_for_mixed_indentation()
	if line.level > 0:
		line.throw_cannot_indent_on_first_line()

	# verify consistent indent
	previous_indent = 0
	for i in range(1, n):
		pline = lines[i-1]
		line = lines[i]

		line.set_tab_used(tab_used)
		line.check_for_mixed_indentation()
		current_indent = line.level

		if line.is_empty:
			continue	
		elif current_indent > previous_indent:
			if not pline.has_colon:
				line.throw_indentation_without_colon()

			if current_indent > previous_indent + 1:
				line.throw_indentation_increased_by_more_than_one_level(pline)

		previous_indent = current_indent

	module.lines = lines
