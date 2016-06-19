from ..config import *

def importpec(linecod):
	s = linecod

	# prep
	if s.is_import_py:
		return
		
	if s.next_linecod_is_packagebol:
		s.packagebol = s.next_linecod
		s.module.package_interpolation.add(s.packagebol)

	else:
		s.packagebol = 0

	if s.is_asis_import:
		s.module.package_interpolation.set_asis_import()

	# importing
	for t in s.atomic_target:
		resolve(s, t)	

	# packagepo pop
	if s.packagebol:
		s.module.package_interpolation.pop()

	if s.is_asis_import:
		s.module.package_interpolation.unset_asis_import()

def resolve(s, t):
	url = t.url(
		skip_if_not_found = 1,
		packagebol = s.packagebol,
		pickle_hash = s.module.package_interpolation.pickle_hash,
	)
		
	if url.found:
		assert_valid_import(t, url.ext)

		x = url.ext

		if x in exts.fy:
			fyR(s, t, url)

		elif x in exts.fort:
			fortR(s, t, url)

		else:
			so_star_import(s, t, url)

	else:
		assert_valid_import(t, '.f90')
		fortR(s, t, url)

def fyR(s, t, url):
	if t.is_ibol:
		fy_aliased_namespace_import(s, t, url)

	elif t.is_namex:
		fy_namex_aliased_namespace_import(s, t, url)

	elif is_star_import(t):
		fy_star_import(s, t, url)

	else:
		fy_slice_import(s, t, url)

def fy_aliased_namespace_import(s, t, url):
	alias = t.rest[0].value
	m = s.module.add_fy_dependency(url)
	s.module_ast[alias] = m

	s > 'use {:s}'.format(m.module_guid)

def fy_namex_aliased_namespace_import(s, t, url):
	m = s.module.add_fy_dependency(url)

	alias = t.value
	s.module_ast[alias] = m

	s > 'use {:s}'.format(m.module_guid)

def fy_star_import(s, t, url):
	m = s.module.add_fy_dependency(url)

	s.module_ast.update(m.ast[0])
	s.module_name.update(m.name[0])

	s > 'use {:s}'.format(m.module_guid)

def fy_slice_import(s, t, url):
	m = s.module.add_fy_dependency(url)
	imported = get_imported(t)

	for name, alias in imported:
		s.module_ast[alias] = m.ast[0][name]
		s.module_name[alias] = m.name[0][name]

	s > 'use {:s}'.format(m.module_guid)

def fortR(s, t, url):
	if url.found:
		url.fy_parent = s.module
		s.module.add_fort_dependency(url)
		name = url.name

	else:
		name = t.value

	b = Buffer()
	b != 'use ' + name

	if is_star_import(t):
		pass

	else:
		imported = get_imported(t)
		b != ', only: '	

		for name, alias in imported:
			b != '{:s}=>{:s}, '.format(alias, name)

		b.rstrip(', ')

	s > b	

def so_star_import(s, t, url):
	s.module.add_so_dependency(url)

def get_imported(t):
	funbol = get_funbol(t)

	imported = []
	for a in funbol.args:
		if a.unit == l.namex:
			name = a.value
			alias = a.value

		elif a.unit == l.opbol:
			name = a.modifier[0].value
			alias = a.modifier[2].value
			
		else:
			funbol.throw(err.cannot_resolve_modifier)

		imported.append([name, alias])

	return imported

def is_star_import(t):
	funbol = get_funbol(t)

	a = funbol.args[0].value

	return a == '*'

def get_funbol(t):
	if t.is_dotbol:
		return t.args[-1]

	else:
		return t

def assert_valid_import(t, ext):
	x = ext
	if x in exts.fy:
		assert_valid_fy_import(t)

	elif x in exts.fort:
		assert_valid_fort_import(t)

	else:
		assert_valid_so_import(t)

def assert_valid_fy_import(t):
	if t.is_namex:
		pass
		# aliased namespace import

	elif t.is_ibol:
		pass
		# aliased namespace import

	else:
		# start or slice import
		funbol = get_funbol(t)
		if not funbol.is_funbol:
			funbol.throw(err.no_element_specified_in_slice_import)

def assert_valid_fort_import(t):
	if t.unit in [l.ibol, l.namex]:
		t.throw(err.only_star_or_slice_import_allowed_for_fortran)

	if t.is_dotbol:
		if not t.args[-1].is_funbol:
			t.throw(err.only_star_or_slice_import_allowed_for_fortran)

	funbol = get_funbol(t)
	if not funbol.args:
		funbol.throw(err.no_element_specified_in_slice_import)

def assert_valid_so_import(t):
	if t.is_ibol or t.is_funbol:
		t.throw(err.only_star_import_allowed_for_shared_library)

	if t.is_dotbol:
		if not t.args[-1].is_funbol:
			t.throw(err.only_star_or_slice_import_allowed_for_fortran)