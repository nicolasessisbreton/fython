class A(Exception):
	def __init__(s, err, *args):
		s.err = err
		s.d = 2323

	@property
	def message(s):
		return 'kawabunga'


	def __str__(s):
		return s.message

class B(A):
	pass		

try:
	raise A('hh', 89)

except B as e:
	print(1)