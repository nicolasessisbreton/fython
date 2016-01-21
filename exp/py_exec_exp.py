s="""
for i in [1, 2]:
	print("print '{:d}'".format(i))
"""

x = exec(s, {'i':1})

print(x)
