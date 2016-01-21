s = r"""
.a.fy
	int cons max_depth = 100
	int cons dotted_length = 300

	char(dotted_length) dimension(max_depth) dotted
	int dimension(max_depth) lineno

	int ndx # frame index

	private:
		max_depth
		dotted_length
		dotted
		lineno
		ndx
		fytbk_reset
		
	def fytbk_reset:
		ndx = 0

	def fytbk_init_frame:
		char(dotted_length) in d
		ndx += 1
		dotted[ndx] = d

	def fytbk_del_frame:
		ndx -= 1

	def fytbk_advance_line:
		int in l
		lineno[ndx] = l
"""

from fython.test import *
shell('rm -rf a/ a.* b.*')

writer(s)

w = load('.a', force=1, release=1, verbose=0)
print(open(w.module.url.fortran_path, 'r').read())
