from ctypes import *
from numpy import array, empty

class FyType:
	def __init__(
		s, 
		value = None,
		shape = [],
		size = 4,
		is_c_pointer = 0,
	):
		s.size = size
		s.basepointer = POINTER(s.basetype)
		s.dtype = '{:s}{:d}'.format(s.dtprefix, s.size*s.size_multiplier)

		s.value = value
		s.shape = shape
		s.is_scalar = 0

		if is_c_pointer:
			s.resolve_c_pointer()

		elif value is not None:
			s.resolve_value()
		else:	
			s.resolve_shape()

		s.resolve_type()

	def resolve_c_pointer(s):
		if isinstance(s.shape, (tuple, list)):
			if len(s.shape) == 0:
				array_type = s.basetype
				s.is_scalar = 1
			else:
				shape = get_value_from_list(s.shape)[::-1]
				array_type = s.basetype * shape[0]
				for i in shape[1:]:
					array_type *= i
		else:
			array_type = s.basetype * get_value(s.shape)

		addr = addressof(s.value.contents)
		s.value = array(array_type.from_address(addr), copy=0)

		if s.is_scalar:
			s.value = s.value.reshape([1])
			
		s.shape = s.value.shape

	def resolve_value(s):
		v = array(s.value, dtype=s.dtype, copy=0)
		if len(v.shape) == 0:
			v = v.reshape([1])
			s.is_scalar = 1

		s.value = v
		s.shape = s.value.shape

	def resolve_shape(s):
		if len(s.shape) == 0:
			s.value = array([0], dtype=s.dtype)
			s.is_scalar = 1
		else:
			s.value = empty(s.shape, dtype=s.dtype)
			
		s.shape = s.value.shape

	def resolve_type(s):
		s.type = s.get_root_type()
		for x in s.shape:
			s.type *= x

		s.type.__array_interface__ = property( lambda self : dict(
			shape = s.shape,
			typestr = s.dtype,
			data = (addressof(self), 0),	
		))

		s.pointer = POINTER(s.type)

		s.ref = s.value.ctypes.data_as(s.basepointer)

	def get_root_type(s):
		return s.basetype

	def in_so(s, so, name):
		x = s.type.in_dll(so, name)
		s.value = array(x, dtype=s.dtype, copy=0)
		s.ref = s.value.ctypes.data_as(s.basepointer)

	def __getitem__(s, slice):
		if s.is_scalar:
			return s.value[0]
		else:
			return s.value[slice]

	def __setitem__(s, slice, value):
		if s.is_scalar:
			s.value[0] = value
		else:
			s.value[slice] = value

	def __str__(s):
		return str(s[:])

	def __repr__(s):
		return str(s)
		
	@property
	def repr(s):
		r = s.__class__.__name__+'\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))
		return r


	def __getstate__(s):
		if s.is_scalar:
			shape = []
			value = s.value[0]
		else:
			shape = s.shape
			value = list(s.value)
		r = [
			shape,
			s.size,
			value,
		]
		return r

	def __setstate__(s, state):
		FyType.__init__(
			s = s,
			value = None,
			shape = state[0],
			size = state[1],
		)
		s[:] = state[2]
		return s

# helper fct
def get_value(x):
	if isinstance(x, FyType):
		return x[:]
	elif isinstance(x, POINTER(c_int)):
		return x.contents.value
	else:
		return x

def get_value_from_list(args):
	r = []
	for x in args:
		r.append(get_value(x))
	return r

# decorator
def fycallback(*args_fytype):
	def decorator(fct):
		args = [POINTER(x.basetype) for x in args_fytype]
		c_fun_dec = CFUNCTYPE(None, *args)
		c_fun = c_fun_dec(fct)
		c_fun_int = cast(c_fun, c_void_p).value
		fct.c_fun_dec = c_fun_dec
		fct.c_fun = c_fun
		fct.fy_address = Int8(c_fun_int)
		return fct
	return decorator

# ---------- particular instance
class Real(FyType):
	name = 'real'
	basetype = c_float
	dtprefix = 'float'
	size_multiplier = 8

class Real8(FyType):
	name = 'real8'
	basetype = c_double
	dtprefix = 'float'
	size_multiplier = 16

class Int(FyType):
	name = 'int'
	basetype = c_int
	dtprefix = 'int'
	size_multiplier = 8

class Int8(FyType):
	name = 'int8'
	basetype = c_long
	dtprefix = 'int'
	size_multiplier = 16

class Char(FyType):
	name = 'char'
	basetype = c_char
	dtprefix = 'S'
	size_multiplier = 1

	def __init__(
		s, 
		size = 200,
		value = None,
		shape = [],
	):
		FyType.__init__(
			s = s,
			size = size,
			value = value, 
			shape = shape,
		)

	def get_root_type(s):
		return s.basetype * s.size

# specialized constructor
# *args gives shape
class IntS(Int):
	def __init__(s, *args, size = 4):
		Int.__init__(
			s = s,
			size = size,
			value = None,
			shape = get_value_from_list(args),
		)

class RealS(Real):
	def __init__(s, *args, size = 4):
		Real.__init__(
			s = s,
			size = size,
			value = None,
			shape = get_value_from_list(args),
		)

class Real8S(Real8):
	def __init__(s, *args, size = 4):
		Real8.__init__(
			s = s,
			size = size,
			value = None,
			shape = get_value_from_list(args),
		)

class CharS(Char):
	def __init__(s, *args, size = 4):
		Char.__init__(
			s = s,
			size = size,
			value = None,
			shape = get_value_from_list(args),
		)

# *args gives value
class IntV(Int):
	def __init__(s, *args, size = 4):
		Int.__init__(
			s = s,
			size = size,
			value = get_value_from_list(args),
			shape = None,
		)

class RealV(Real):
	def __init__(s, *args, size = 4):
		Real.__init__(
			s = s,
			size = size,
			value = get_value_from_list(args),
			shape = None,
		)

class Real8V(Real8):
	def __init__(s, *args, size = 4):
		Real8.__init__(
			s = s,
			size = size,
			value = get_value_from_list(args),
			shape = None,
		)

class CharV(Char):
	def __init__(s, *args, size = 4):
		Char.__init__(
			s = s,
			size = size,
			value = get_value_from_list(args),
			shape = None,
		)

# v=list gives value
class IntL(Int):
	def __init__(s, value, size = 4):
		Int.__init__(
			s = s,
			size = size,
			value = value,
			shape = None,
		)

class RealL(Real):
	def __init__(s, value, size = 4):
		Real.__init__(
			s = s,
			size = size,
			value = value,
			shape = None,
		)

class Real8L(Real8):
	def __init__(s, value, size = 4):
		Real8.__init__(
			s = s,
			size = size,
			value = value,
			shape = None,
		)

class CharL(Char):
	def __init__(s, value, size = 4):
		Char.__init__(
			s = s,
			size = size,
			value = value,
			shape = None,
		)

# v:c pointer
class IntP(Int):
	def __init__(s, value, shape=[], size = 4):
		Int.__init__(
			s = s,
			size = size,
			value = value,
			shape = shape,
			is_c_pointer = 1,
		)

class Int8P(Int8):
	def __init__(s, value, shape=[], size = 4):
		Int8.__init__(
			s = s,
			size = size,
			value = value,
			shape = shape,
			is_c_pointer = 1,
		)

class RealP(Real):
	def __init__(s, value, shape=[], size = 4):
		Real.__init__(
			s = s,
			size = size,
			value = value,
			shape = shape,
			is_c_pointer = 1,
		)

class Real8P(Real8):
	def __init__(s, value, shape=[], size = 4):
		Real8.__init__(
			s = s,
			size = size,
			value = value,
			shape = shape,
			is_c_pointer = 1,
		)

class CharP(Char):
	def __init__(s, value, shape=[], size = 4):
		Char.__init__(
			s = s,
			size = size,
			value = value,
			shape = shape,
			is_c_pointer = 1,
		)
