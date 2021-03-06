import subprocess
import re
from . import exception as err
from .path import *
from .data import *

guid_length = 10

# io
fyio_default_unit = '608597210'

# interpolant
fyinterpolant_url = 'fython.interpolant.interpolant'

# class property
getpfx = 'g3jk28_'
setpfx = 's84kd9_'

# implicit none
implicit_none = '\nimplicit none\n'

# fortran compiler
class fyfc_ifort(Data):
	cmd = 'ifort'

	prefix = ''
	infix = '_mp_'
	suffix = '_'

	debug = """
	-g 
	-traceback
	-gen-interfaces 
	-warn all
	-check all
	-fpe0
	-ftrapuv
	""".replace('\n', ' ')

	release = """
	-fast
	""".replace('\n', ' ')


	link = ''

	error_regex = '(error #|ld:)'
	warning_regex = '(warning #|remark #)'


class fyfc_gfortran(Data):
	cmd = 'gfortran'
	prefix = '__'
	infix = '_MOD_'
	suffix = ''

	debug = """
	-g 
	-fbacktrace
	-Wall
	-fbounds-check
	-ffpe-trap=zero,overflow
	""".replace('\n', ' ')

	release = """
	-O3
	""".replace('\n', ' ')


	link = ''

	error_regex = '(Error:|ld:)'
	warning_regex = 'warning'

def use_ifort():
	global fyfc
	fyfc.update(fyfc_ifort)

def use_gfortran():
	global fyfc
	fyfc.update(fyfc_gfortran)

def set_compiler(
	cmd,
	prefix,
	infix,
	suffix,
	debug,
	release,
	link,
	error_regex,
	warning_regex,
):	
	global fyfc
	fyfc.update( Data(
		cmd = cmd,
		prefix = prefix,
		infix = infix,
		suffix= suffix,
		debug = debug.replace('\n', ''),
		release = release.replace('\n', ''),
		link = link.replace('\n', ''),
		error_regex = error_regex,
		warning_regex = warning_regex,
	))

class FyFC(Data):
	def __init__(s):
		s.fortran_compiler_setted = 0

	def update(s, d):
		s.fortran_compiler_setted = 1
		s.__dict__.update(d.__dict__)

	def is_error(s, msg):
		return re.search(s.error_regex, msg)

	def is_warning(s, msg):
		return re.search(s.warning_regex, msg)

	@property
	def assert_compiler_setted(s):
		if not s.fortran_compiler_setted:
			raise err.no_fortran_compiler_found("use 'fython.set_compiler' to set the compiler manually") 

fyfc = FyFC()

def find_compiler():
	try:
		subprocess.check_output('ifort --version', shell=1)
		use_ifort()

	except subprocess.CalledProcessError:
		subprocess.check_output('gfortran --version', shell=1)
		use_gfortran()

	except subprocess.CalledProcessError:
		pass

	except Exception as e:
		raise e 

# various compilers
def use_mkl():
	set_compiler(
		cmd = 'ifort',
		prefix = '',
		infix = '_mp_',
		suffix = '_',
		debug = """
			-g 
			-traceback
			-gen-interfaces 
			-warn all
			-check all
			-fpe0
			-ftrapuv
			-I/opt/intel/mkl/include
		""",
		release = """
			-fast
			-I/opt/intel/mkl/include
		""",
		link = """
			-L/opt/intel/mkl/lib/intel64 
			-lmkl_intel_lp64 
			-lmkl_core
			-lmkl_sequential 
			-lpthread 
			-lm
		""",
		error_regex = '(error #|ld:)',
		
		warning_regex = '(warning #|remark #)',
	)


	# needed to load mkl
	# see: https://answers.launchpad.net/dolfin/+question/205219
	import ctypes
	ctypes.CDLL('libmkl_rt.so', ctypes.RTLD_GLOBAL)

def use_mkl_blas_lapack():
	set_compiler(
		cmd = 'ifort',
		prefix = '',
		infix = '_mp_',
		suffix = '_',
		debug = """
			-g 
			-traceback
			-gen-interfaces 
			-warn all
			-check all
			-fpe0
			-ftrapuv
			-qopenmp
			-I/opt/intel/mkl/include/intel64/lp64
			-I/opt/intel/mkl/include
		""",
		release = """
			-fast
			-qopenmp
			-I/opt/intel/mkl/include/intel64/lp64
			-I/opt/intel/mkl/include
		""",
		link = """
			/opt/intel/mkl/lib/intel64/libmkl_blas95_lp64.a
			/opt/intel/mkl/lib/intel64/libmkl_lapack95_lp64.a
			-L/opt/intel/mkl/lib/intel64
			-lmkl_intel_lp64
			-lmkl_core
			-lmkl_intel_thread
			-lpthread
			-lm
			-ldl	
		""",
		error_regex = '(error #|ld:)',
		
		warning_regex = '(warning #|remark #)',
	)


	# needed to load mkl
	# see: https://answers.launchpad.net/dolfin/+question/205219
	import ctypes
	ctypes.CDLL('libmkl_rt.so', ctypes.RTLD_GLOBAL)
	ctypes.CDLL('/opt/intel/lib/intel64/libiomp5.so', ctypes.RTLD_GLOBAL)

def use_mkl_blas_lapack_gurobi():
	set_compiler(
		cmd = 'ifort',
		prefix = '',
		infix = '_mp_',
		suffix = '_',
		debug = """
			-g 
			-traceback
			-gen-interfaces 
			-warn all
			-check all
			-fpe0
			-ftrapuv
			-qopenmp
			-I/opt/intel/mkl/include/intel64/lp64
			-I/opt/intel/mkl/include
		""",
		release = """
			-fast
			-qopenmp
			-I/opt/intel/mkl/include/intel64/lp64
			-I/opt/intel/mkl/include
		""",
		link = """
			/opt/intel/mkl/lib/intel64/libmkl_blas95_lp64.a
			/opt/intel/mkl/lib/intel64/libmkl_lapack95_lp64.a
			-L/opt/intel/mkl/lib/intel64
			-L/opt/gurobi751/linux64/lib
			-lgurobi75
			-lmkl_intel_lp64
			-lmkl_core
			-lmkl_intel_thread
			-lpthread
			-lm
			-ldl	
		""",
		error_regex = '(error #|ld:)',
		
		warning_regex = '(warning #|remark #)',
	)


	# needed to load mkl
	# see: https://answers.launchpad.net/dolfin/+question/205219
	import ctypes
	ctypes.CDLL('libmkl_rt.so', ctypes.RTLD_GLOBAL)
	ctypes.CDLL('/opt/intel/lib/intel64/libiomp5.so', ctypes.RTLD_GLOBAL)

def use_mkl_gurobi():
	set_compiler(
		cmd = 'ifort',
		prefix = '',
		infix = '_mp_',
		suffix = '_',
		debug = """
			-g 
			-traceback
			-gen-interfaces 
			-warn all
			-check all
			-fpe0
			-ftrapuv
			-qopenmp
			-I/opt/intel/mkl/include/intel64/lp64
			-I/opt/intel/mkl/include
		""",
		release = """
			-fast
			-qopenmp
			-I/opt/intel/mkl/include/intel64/lp64
			-I/opt/intel/mkl/include
		""",
		link = """
			-L/opt/intel/mkl/lib/intel64
			-L/opt/gurobi751/linux64/lib
			-lgurobi75
			-lmkl_intel_lp64
			-lmkl_core
			-lmkl_intel_thread
			-lpthread
			-lm
			-ldl	
		""",
		error_regex = '(error #|ld:)',
		
		warning_regex = '(warning #|remark #)',
	)


	# needed to load mkl
	# see: https://answers.launchpad.net/dolfin/+question/205219
	import ctypes
	ctypes.CDLL('libmkl_rt.so', ctypes.RTLD_GLOBAL)
	ctypes.CDLL('/opt/intel/lib/intel64/libiomp5.so', ctypes.RTLD_GLOBAL)


