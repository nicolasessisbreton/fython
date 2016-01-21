def f(*args, **kwargs):
	print(args)
	print(kwargs)


f(1)
f(x=1, y=1, z=2)