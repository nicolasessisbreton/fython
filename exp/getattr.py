class A:
	def __getattr__(s, n):
		print(n)
		return s.call

	def call(s):
		print(1)



a = A()

# a.x

a.y()