import re

code = """XabX
"""

p = r'a(?:b)(X)'

print(
	# re.findall(p, code)
)

m = re.match(p, code)
print(
	# m.group
)

def f(m):
	print(11, m.group(1))

print(
	re.sub(p, f, code)
)

