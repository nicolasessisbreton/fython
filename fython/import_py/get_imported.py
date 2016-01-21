def get_imported(funbol):
	imported = []
	for a in funbol.args:
		if a.is_namex:
			name = a.value
			alias = a.value

		elif a.is_opbol:
			name = a.modifier[0].value
			alias = a.modifier[2].value
			
		else:
			funbol.throw(err.cannot_resolve_modifier)

		imported.append([name, alias])

	return imported