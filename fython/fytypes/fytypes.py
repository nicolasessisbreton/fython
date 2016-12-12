from ctypes import *
from numpy import array, empty

class FyType:
	def __init__(
		s, 
		value = None,
		shape = [],
		size = 4,
	):
		s.size = size
		s.basepointer = POINTER(s.basetype)
		s.dtype = '{:s}{:d}'.format(s.dtprefix, s.size*s.size_multiplier)

		s.value = value
		s.shape = shape
		s.is_scalar = 0

		if value is not None:
			s.resolve_value()
		else:	
			s.resolve_shape()

		s.resolve_type()

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

	def __repr__(s):
		r = s.__class__.__name__+'\n'
		for key, item in s.__dict__.items():
			r += '\t{:s} {:s}\n'.format(key, repr(item))
		return r


	def get_value_from_args(s, args):
		shape = []
		
		for x in args:
			if isinstance(x, FyType):
				shape.append( x[:] )
			else:
				shape.append( x )

		return shape

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
			shape = s.get_value_from_args(args),
		)

class RealS(Real):
	def __init__(s, *args, size = 4):
		Real.__init__(
			s = s,
			size = size,
			value = None,
			shape = s.get_value_from_args(args),
		)

class Real8S(Real8):
	def __init__(s, *args, size = 4):
		Real8.__init__(
			s = s,
			size = size,
			value = None,
			shape = s.get_value_from_args(args),
		)

class CharS(Char):
	def __init__(s, *args, size = 4):
		Char.__init__(
			s = s,
			size = size,
			value = None,
			shape = s.get_value_from_args(args),
		)

# *args gives value
class IntV(Int):
	def __init__(s, *args, size = 4):
		Int.__init__(
			s = s,
			size = size,
			value = s.get_value_from_args(args),
			shape = None,
		)

class RealV(Real):
	def __init__(s, *args, size = 4):
		Real.__init__(
			s = s,
			size = size,
			value = s.get_value_from_args(args),
			shape = None,
		)

class Real8V(Real8):
	def __init__(s, *args, size = 4):
		Real8.__init__(
			s = s,
			size = size,
			value = s.get_value_from_args(args),
			shape = None,
		)

class CharV(Char):
	def __init__(s, *args, size = 4):
		Char.__init__(
			s = s,
			size = size,
			value = s.get_value_from_args(args),
			shape = None,
		)