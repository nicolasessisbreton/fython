opener = '\nif ( <fytbk_advance_line>({:d}) ) then\n'
closer = '\nend if\n'

def open_line(lineno):
	return opener.format(lineno)

def close_line():
	return closer
