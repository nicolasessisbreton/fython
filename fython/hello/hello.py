from ..config import *
from ..load import *

def hello():
	m = load(
		url = 'fython.hello.hello',
		force = 0,
		release = 0,
	)

	prefix = m.hello(size=100, shape=[])

	r = '{:s} {:s}/fython/hello/__pycache__/fycache'.format(
		prefix[:].decode('utf-8').strip(),
		fython_root,
	)

	return r
