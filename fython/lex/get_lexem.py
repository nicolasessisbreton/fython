def get_lexem(lexer):
	r =[]
	t = lexer.token()
	while t:
		r.append(t)
		t = lexer.token()
	return r