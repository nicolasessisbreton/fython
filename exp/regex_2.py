import re

code = """XabX
--------^
"""

p = r'^-*\^$'

print(
	# re.findall(p, code)
)

m = re.match(p, code)
print(
	# m.group
)

def f(m):
	print(11, m.group(0))

print(
	re.sub(p, 'aa', code, re.M)
)

