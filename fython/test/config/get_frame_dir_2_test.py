from fython.test import *

shell('rm -rf a/ b/ a.py b.py c.py')

writer("""
.a.a.py
	from fython.config import *
	def f():
		return get_frame_dir(1)

.b.b.py
	import ~..a.a.py as a

.c.py
	from ~.b.b.py import *
	print(a.f())

""")


# imp('.c')