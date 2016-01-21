from fython.config.trim import trim as _trim

_write_cache = ''

def write(source, *args, end='\n', **kwargs):
	global _write_cache
	source = _trim(source)
	_write_cache += source.format(*args, **kwargs)
	_write_cache += end
	return _write_cache

def _reset_cache():
	global _write_cache
	_write_cache = ''
