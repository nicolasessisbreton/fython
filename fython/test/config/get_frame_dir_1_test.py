from fython.test import *

shell('rm -rf a/ a.py d.py')

writer("""
.a.b.c.d.a.py
	from ..config import *
	def f():
		return get_frame_dir(1)

.d.py
	import ~.a.b.c.d.a.py	as a
	print(a.f())

""")


# imp('.d')