from ..config import *
from .get_imported import get_imported

def import_py(linecod):
	m = linecod.modifier[1]

	if m.is_namex:
		namexR(m, linecod)

	elif m.is_funbol:
		funbolR(m, linecod)

	elif m.is_dotbol:
		dotbolR(m, linecod)

	elif m.is_ibol:
		ibolR(m, linecod)

	elif m.is_childcod:
		pass # nothing to do, not supported for the moment, but is easy to add, see importpec.py: line 15
	else:
		m.throw(err.cannot_resolve_modifier)

def namexR(n, linecod):
	url = n.url(
		cwd = n.module_dir,
		ext = exts.py,
		skip_if_not_found = 1,
	)

	if not url.found:
		return

	r = 'import ' + url.dotted

	n.module.eval_import_statement(r)

	linecod.is_import_py = 1

def funbolR(f, linecod):
	url = f.url(
		cwd = f.module_dir,
		ext = exts.py,
		skip_if_not_found = 1,
	)

	if not url.found:
		return

	if f.args[0].value == '*':
		r = 'from {:s} import *'.format(url.dotted)

	else:
		imported = get_imported(f)
		b = Buffer(newline=' ')

		b += 'from {:s} import ('.format(url.dotted)

		for name, alias in imported:
			b += '{:s} as {:s},'.format(name, alias)

		b.rcut(1)
		b += ')'

	f.module.eval_import_statement(r)

	linecod.is_import_py = 1

def dotbolR(d, linecod):
	url = d.url(
		cwd = d.module_dir,
		ext = exts.py,
		skip_if_not_found=1,
	)

	if not url.found:
		return

	f = d.modifier[-1]

	if not f.is_funbol:
		s.throw(err.cannot_resolve_modifier)

	if f.args[0].value == '*':
		r = 'from {:s} import *'.format(url.dotted)

	else:
		imported = get_imported(f)
		b = Buffer(newline=' ')

		b += 'from {:s} import ('.format(url.dotted)

		for name, alias in imported:
			b += '{:s} as {:s},'.format(name, alias)

		b.rcut(1)
		b += ')'

		r = str(b)

	f.module.eval_import_statement(r)

	linecod.is_import_py = 1

def ibolR(m, linecod):
	target = m.target
	alias = m.rest[0]

	if target.is_namex:
		namex_alias(target, alias, linecod)

	elif target.is_dotbol:
		dotbol_alias(target, alias, linecod)

	else:
		m.throw(err.cannot_resolve_modifier)

def namex_alias(n, a, linecod):
	url = n.url(
		cwd = n.module_dir,
		ext = exts.py,
		skip_if_not_found = 1,
	)

	if not url.found:
		return

	r = 'import {:s} as {:s}'.format(url.dotted, a.value)

	n.module.eval_import_statement(r)

	linecod.is_import_py = 1

def dotbol_alias(d, a, linecod):
	url = d.url(
		cwd = d.module_dir,
		ext = exts.py,
		skip_if_not_found=1,
	)

	if not url.found:
		return

	r = 'import {:s} as {:s}'.format(url.dotted, a.value)

	d.module.eval_import_statement(r)

	linecod.is_import_py = 1
	