from importlib import import_module
from ..config import *
from .unaryr import unaryR
from .genericr import genericR

def resolve(linecod):
	if linecod.is_packagebol:
		return	

	elif linecod.has_ibol:
		r = l.iruc

	elif linecod.modifier[1].is_newlinex:
		r = unaryR(linecod)

	else:
		r = genericR(linecod)

	url = get_module_url(r)
	m = import_module(url)
	f = getattr(m, r)

	try:
		f(linecod)	

	except err.FyException as e:
		raise e

	except Exception as e:
		error = linecod.throw(
			err.resolution_error,
			resolution_error = repr(e),
			return_only = 1,
		)

		error.__traceback__ = e.__traceback__

		raise error from None


def get_module_url(name):
	if name.endswith(l.spec_suffix):
		return 'fython.spec.{:s}'.format(name)

	else:
		return 'fython.instruction.{:s}'.format(name)
