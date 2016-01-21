a = type('a_fyerr', (Exception,), {})

try:
	raise a('aa')

except Exception as e:
	print(type(e))