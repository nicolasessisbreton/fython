s = """
.a.fy
	indent start:
		but

		was stop previously
			incorrect indent
"""

from fython.test import *

shell('rm -rf a/ a.* b.*')

writer(s)


try:
	w = load('.a', force=1, release=1, verbose=0)

except Exception as e:
	print(e)
	assert_equal(1, 'indentation without colon' in str(e))

