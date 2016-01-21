import os
from importlib import import_module
from fython.config import *

n = len(fython_root)
cwd = get_frame_dir()

for dirpath, dirnames, filenames in os.walk(cwd):
	for f in filenames:
		name, ext = os.path.splitext(f)

		path = os.path.abspath('{:s}/{:s}'.format(dirpath, name))
		path = path[n+1:]
		dotted = path.replace('/', '.')

		if name.startswith('_'):
			continue
		if ext != '.py':
			continue
		if name[:3] != 'all' and 'test' in name:
			print('--', dotted, '--')
			import_module(dotted)
			print()

print('---')
print('All tests passed.')