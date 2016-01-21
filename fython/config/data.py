class Data:
	def __init__(s, **kwargs):
		s.__dict__.update(kwargs)

	def __repr__(s):
		r = s.__class__.__name__+'\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))
		return r
