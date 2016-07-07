import re
import sys
from os.path import abspath, basename, dirname, exists, getmtime, splitext
from .data import Data
from . import extension as exts
from .mkdir import mkdir
from . import exception as err
from .buffer import Buffer
from .compilation import fyfc
from .debugging import *

relpath = re.compile(r'(\.+)([^\.].*)')

class Url:
	def __init__(
		s,
		url,
		cwd,
		ext,
		path_only = 0,
		skip_if_not_found = 0,
		packagebol = 0,
		release = 0,
		pickle_hash = '',
	):
		s.url = url
		s.cwd = cwd
		s.path_only = path_only
		s.skip_if_not_found = skip_if_not_found
		s.found = 1
		s.packagebol = packagebol	
		s.release = release
		s.pickle_hash = pickle_hash

		s.fy_parent = None
		s.is_noforce = 0		
		
		if isinstance(ext, list):
			s.exts = ext
		else:
			s.exts = [ext]

		if s.url[0] == '.':
			s.relative()
		else:
			s.fully_qualified()


	def relative(s):
		dot, name = relpath.findall(s.url)[0]

		root = s.cwd
		for i in range(len(dot)-1):
			root = dirname(root)

		root = root.rstrip('/')
		
		s.set_filename(name)

		if s.find(root):
			s.dotted = s.get_dotted_name()
			s.dotted_tree = s.get_dotted_tree()
			return 

		s.throw_module_not_found()

	def fully_qualified(s):
		s.dotted = s.url
		s.dotted_tree = s.get_dotted_tree()

		s.set_filename(s.dotted)

		for root in sys.path:
			root = abspath(root)
			if s.find(root):
				return 

		s.throw_module_not_found()

	def set_filename(s, target):
		s.filename = '/'.join(target.split('.'))

	def find(s, root):
		for ext in s.exts:
			p = '{:s}/{:s}{:s}'.format(root, s.filename, ext)

			if s.path_only:
				t = root
			else:
				t = p

			if exists(t):
				s.ext = ext
				s.path = p
				s.package_root = root
				s.module_dir = dirname(p)
				s.name_ext = basename(p)
				s.name = splitext(s.name_ext)[0]

				if s.path_only:
					return 1

				elif s.ext in exts.py:
					return 1

				elif s.ext in exts.so:
					s.object_name = s.name_ext
					s.object_path = s.path
					s.fycache_dir = ''
					s.pickle = s.path
					return 1

				# compilation path helper		
				s.fycache_dir = s.module_dir + '/__pycache__'
				mkdir(s.fycache_dir)
				s.fycache_dir += '/fycache'
				mkdir(s.fycache_dir)

				# hierarchy of build kinds
				s.fycache_dir += '/' + fyfc.cmd # compiler used
				mkdir(s.fycache_dir)

				if s.release:
					s.fycache_dir += '/release'
					mkdir(s.fycache_dir)
						
				else:
					s.fycache_dir += '/debug'
					mkdir(s.fycache_dir)

				# object
				s.object_name = s.name + s.pickle_hash + '.o'
				s.object_path = '{:s}/{:s}'.format(s.fycache_dir, s.object_name)

				# fortran
				if s.ext in exts.fort:
					s.fortran_name = s.name_ext 

				else:
					s.fortran_name = s.name + s.pickle_hash + '.f90'
					
				s.fortran_path = '{:s}/{:s}'.format(s.fycache_dir, s.fortran_name)

				# so
				s.so_name = s.name + s.pickle_hash + '.so'
				s.so_path = '{:s}/{:s}'.format(s.fycache_dir, s.so_name)
				
				# pickle
				s.pickle = '{:s}/{:s}{:s}.pickle'.format(
					s.fycache_dir, 
					s.name,
					s.pickle_hash,
				)

				return 1

	def get_dotted_name(s):
		r = ''
		found = 0
		for p in sys.path:
			if s.path.startswith(p):
				n = len(p)
				p = s.path[n+1:]
				p = splitext(p)[0]
				p = p.replace('/', '.')
				if len(p) > len(r):
					r = p
		if r:
			return r
		else:
			s.throw(err.package_not_found)

	def throw(s, error):
		b = Buffer()
		b += 'url {:s}'.format(s.url)
		b += "working directory '{:s}'".format(s.cwd)
		b += 'extensions considered:'
		b += ', '.join(s.exts)
		raise(error(b))
		
	def get_dotted_tree(s):
		part = s.dotted.split('.')
		t = []

		r = part[0]
		t.append(r)

		for p in part[1:]:
			r += '.' + p
			t.append(r)

		return t

	def throw_module_not_found(s):
		s.found = 0
		if s.skip_if_not_found:
			return
		else:
			s.throw(err.module_not_found)

	@property
	def is_up_to_date(s):
		if s.ext in exts.so:
			return 1

		elif exists(s.pickle):
			cache = getmtime(s.pickle)
			code = getmtime(s.path)
			r = cache > code
			return r

	@property
	def rep(s):
		return s.__repr__()
		
	def __repr__(s):
		if hasattr(s, 'dotted'):
			return 'Url({:s})'.format(s.dotted)

		else:
			return 'Url({:s})'.format(s.url)

	@property
	def nfo(s):
		r = repr(s) + '\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))

		return r
