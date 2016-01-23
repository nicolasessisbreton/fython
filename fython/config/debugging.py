from __future__ import print_function

def xip(*args):
	for a in args:
		print(a, end=' ')
	print('')

def xep(*args):
	for a in args:
		print(repr(a), end=' ')
	print('')


def xfo(*args):
	for a in args:
		if hasattr(a, 'nfo'):
			print(a.nfo, end=' ')
		else:
			print(repr(a), end=' ')
	print('')
