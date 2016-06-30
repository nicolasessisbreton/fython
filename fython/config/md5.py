from hashlib import md5 as m

def md5(s):
	return m( s.encode('utf-8') ).hexdigest()