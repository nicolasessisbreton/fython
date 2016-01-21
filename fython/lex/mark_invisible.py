from .config import *

def mark_invisible(module):
	lines = module.lines
	
	r = []
	previous_indent = 0

	for i in range(len(lines)):
		line = lines[i]
		
		if line.is_empty:
			continue

		line.remove_colon()
		
		current_indent = line.level

		pre = linefeedx.format(line.lineno)

		if current_indent > previous_indent:
			r[-1] = r[-1][:-len_newlinex] # pop newlinex on previous line
			pre = indentx + pre

		elif current_indent < previous_indent:
			d = previous_indent - current_indent
			pre = dedentx*d + pre

		line = pre + line.line + newlinex

		r.append(line)

		previous_indent = current_indent

	if previous_indent > 0:
		final_dedent = dedentx * previous_indent
		r.append(final_dedent)
	
	s = ''.join(r)

	s = bofx + s + eofx

	module.source_with_invisible = s

	if module.verbose.source_with_invisible:
		module.verbose_tag('source with invisible')
		print(module.source_with_invisible)