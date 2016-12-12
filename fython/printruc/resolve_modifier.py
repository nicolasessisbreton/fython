from ..config import *
from os import getcwd
from os.path import abspath

def resolve_modifier(p):
	for m in p.linecod.modifier_only:
		if m.is_stringx:
			resolve_string(p, m)

		elif m.is_dotbol:
			resolve_dotbol(p, m)

		elif m.is_numberx:
			p.unit = m
			
		elif m.is_namex:
			if m.value == 'c':
				p.advance = ', advance="no"'

			else:
				p.unit = m

		elif m.is_funbol:
			resolve_funbol(p, m)

		else:
			p.throw(err.cannot_resolve_modifier, modifier=repr(m))

	# handle unspecified unit
	if p.path:
		if p.unit == '*':
			p.unit = fyio_default_unit

def resolve_string(p, s):
	p.path = abspath(s.value)
	p.path = "'" + p.path + "'"

def resolve_dotbol(p, d):
	url = d.url(
		ext = exts.out,
		cwd = getcwd(),
		path_only = 1,
	)

	p.path = "'" + url.path + "'"

def resolve_namex(p, m):
	p.path = m

def resolve_funbol(p, f):
	n = f.value

	if n == 'url':
		resolve_dotbol(p, f.args[0])

	elif n == 'path':
		resolve_path(p, f.args[0])

	elif n == 'mode':
		p.mode = f.args[0].value

	elif n == 'unit':
		p.unit = f.args[0]

	else:
		p.throw(err.cannot_resolve_modifier, modifier=repr(m))
		

def resolve_path(p, h):
	if h.is_stringx:
		resolve_string(p, h)

	elif h.is_namex:
		resolve_namex(p, h)

	else:
		p.throw(err.cannot_resolve_modifier, path_argument=repr(h))