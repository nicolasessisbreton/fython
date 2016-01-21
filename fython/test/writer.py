import sys
from os.path import abspath, exists
from importlib import invalidate_caches
from ..config import *

dotted_re = re.compile('~[\w\.]+')

def writer(s):
	cwd = get_frame_dir(1) + '/'
	
	s = s.split('\n')
	n = len(s)

	path = []
	ndx = []

	# first and last line ignored
	for i in range(n):
		line = s[i]

		if not line:
			continue

		if line[0] == '#':
			s[i] = ''
			continue

		if line[0] not in ' \t\n':
			p = get_path(line, cwd)
			path.append(p)
			ndx.append(i)

	ndx.append(n)

	# writing
	for i in range(len(path)):
		p = path[i]

		root = [dirname(p)]
		while not exists(root[0]):
			r = dirname(root[0])
			root.insert(0, r)

		for r in root:
			mkdir(r)

		a = ndx[i]
		b = ndx[i+1]
		c = '\n'.join(s[a:b])
		c = trim(c) # cuts the first line

		c = dotted_re.sub(lambda m : dotter(m, cwd), c)
		
		open(p, 'w').write(c)

def dotter(match, cwd):
	# ~.a.a.py
	c = match.group(0)
	c = c[1:]
	ndx = c.rfind('.')
	name = c[:ndx]
	ext = c[ndx:]
	url = Url(
		url = name,
		cwd = cwd,
		ext = [ext],
	)
	return url.dotted

def get_path(line, cwd):
	p = line.strip()

	ndx = p.rfind('.')
	name = p[:ndx]
	ext = p[ndx:]
	url = Url(
		url = name,
		cwd = cwd,
		ext = [ext],
		path_only = 1,
	)

	# clean python cache
	if url.ext in exts.py:
		sys.modules.pop(url.dotted, None)

	return url.path
