from ctypes import cdll
from ..config import *
from fython.fytypes import *
from fython.traceback import stack_trace

typemapping = dict(
	real = Real,
	integer = Int,
	character = Char,
)

class PyWrapper(Data):
	def __init__(s, module, run_main, so_path=None):
		s.run_main = run_main

		if so_path:
			s.so_path = so_path

		else:
			s.so_path = module.url.so_path

		s.module_guid = module.module_guid
		s.module = module
	
		s.module_name = module.name[0]	
		
		s.has_main = module.has_main	
		s.release = module.release
		s.debug = module.debug

		s.entity = {}
		for alias , u in module.ast[0].items():
			if u.is_varpec:
				if u.is_wrappable:
					s.add_varpec(alias, u)

			elif u.is_routpec:
				if u.is_wrappable:
					s.add_routpec(alias, u)

			elif u.is_module:
				s.add_module(alias, u)

		if s.debug:
			s.tbk_ndx_name = s.get_name_in_tbk(module, 'ndx')			
			s.tbk_dotted_name = s.get_name_in_tbk(module, 'dotted')			
			s.tbk_lineno_name = s.get_name_in_tbk(module, 'lineno')			
			s.tbk_last_error_name = s.get_name_in_tbk(module, 'last_error')			
			s.tbk_verbose_name = s.get_name_in_tbk(module, 'verbose')			
			s.tbk_reset_name = s.get_name_in_tbk(module, 'reset')

		s.connect()

	def add_varpec(s, alias, v):
		guid = s.module_name[alias]
		s.entity[alias] = Data(
			alias = alias,
			unit = l.varpec,
			typename = v.typename,
			so_name = s.get_name_in_so(v.module.module_guid, guid),
		)

	def add_routpec(s, alias, r):
		argument = r.argument + []
		guid = s.module_name[alias]

		s.entity[alias] = Data(
			alias = alias,
			unit = l.routpec,
			nb_argument = len(argument),
			argument = argument,
			so_name = s.get_name_in_so(r.module.module_guid, guid),
		)

	def add_module(s, alias, m):
		s.entity[alias] = Data(
			unit = l.module,
			wrapper = PyWrapper(m, run_main=0, so_path=s.so_path),
		)

	def connect(s):
		s.so = cdll.LoadLibrary(s.so_path)

		if s.debug:
			s.tbk_ndx = Int()
			s.tbk_dotted = Char(size=fytbk.dotted_size, shape=[fytbk.max_depth])
			s.tbk_lineno = Int(shape=[fytbk.max_depth])
			s.tbk_last_error = Char(size=fytbk.last_error_size)
			s.tbk_verbose = Int()

			s.tbk_ndx.in_so(s.so, s.tbk_ndx_name)
			s.tbk_dotted.in_so(s.so, s.tbk_dotted_name)
			s.tbk_lineno.in_so(s.so, s.tbk_lineno_name)
			s.tbk_last_error.in_so(s.so, s.tbk_last_error_name)
			s.tbk_verbose.in_so(s.so, s.tbk_verbose_name)

		if s.has_main and s.run_main:
			s.main()

	def verbose(s):
		s.tbk_verbose[:] = 1

	def quiet(s):
		s.tbk_verbose[:] = 0

	# s(): get object in so
	def __call__(s, name):
		return s.so.__getattr__(name)

	def main(s):
		n = '{prefix:s}{guid:s}{infix:s}{guid:s}_main{suffix}'.format(
			prefix = fyfc.prefix,
			guid = s.module_guid, 
			infix = fyfc.infix,
			suffix = fyfc.suffix,
		)

		if s.debug:
			s(s.tbk_reset_name)()

		s(n)()

	def __getattr__(s, name):
		if name not in s.entity:
			s.throw(err.name_not_found_in_fython_module, name=name)

		e = s.entity[name]

		if e.unit == l.varpec:
			return lambda size=4, shape=[] : s.call_var(e, size, shape)

		elif e.unit == l.routpec:
			return lambda *args, **kwargs : s.call_rout(e, *args, **kwargs)
			
		else:
			# module
			return e.wrapper

	def call_var(s, v, size, shape):
		r = typemapping[v.typename.value](size=size, shape=shape)
		r.in_so(s.so, v.so_name)
		return r

	def call_rout(s, rout, *args, **kwargs):
		if args and kwargs:
			s.throw(err.cannot_mix_args_and_kwargs, function_name=rout.alias)

		if s.debug:
			s(s.tbk_reset_name)()

		if args:
			if len(args) != rout.nb_argument:
				s.throw(err.nb_of_arguments_mismatch, nb_received=len(args), nb_expected=rout.nb_argument, function_name=rout.alias)

			s(rout.so_name)(*get_arg_ref(args))

		elif kwargs:
			if len(kwargs) != rout.nb_argument:
				s.throw(err.nb_of_arguments_mismatch, nb_received=len(kwargs), nb_expected=rout.nb_argument, function_name=rout.alias)

			args = s.order_args(rout, kwargs)

			s(rout.so_name)(*get_arg_ref(args))

		else:
			if rout.nb_argument != 0:
				s.throw(err.nb_of_arguments_mismatch, nb_received=0, nb_expected=rout.nb_argumen, function_name=rout.alias)

			s(rout.so_name)()	

		if s.debug:
			if s.tbk_ndx[:] > 0:
				stack_trace(
					last_error = s.tbk_last_error[:],
					ndx = s.tbk_ndx[:],
					dotted = s.tbk_dotted[:],
					lineno = s.tbk_lineno[:],
				)
	
	def get_name_in_so(s, module_guid, varname_guid):
		return '{prefix:s}{modname:s}{infix:s}{varname_guid:s}{suffix:s}'.format(
			prefix = fyfc.prefix,
			modname = module_guid,
			infix = fyfc.infix,
			varname_guid = varname_guid,
			suffix = fyfc.suffix,
		)

	def get_name_in_tbk(s, module, name):
		m = module.stack.fytbk
		
		r = '{prefix:s}{modname:s}{infix:s}{varname:s}{suffix:s}'.format(
			prefix = fyfc.prefix,
			modname = m.module_guid,
			infix = fyfc.infix,
			varname = m.name[0][name],
			suffix = fyfc.suffix,
		)

		return r

	def order_args(s, rout, kwargs):
		args = []
		for x in rout.argument:
			args.append(kwargs[x])
		return args

	def throw(s, error_type, **kwargs):
		s.module.throw(error_type, **kwargs)

def get_arg_ref(args):
	r = []
	for a in args:
		r.append(a.ref)
	return r