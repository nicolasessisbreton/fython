from .printruc_type import PrintRuc
from .resolve_modifier import resolve_modifier
from .open_file import open_file
from .make_print import make_print
from .close_file import close_file

def printruc(s):
	p = PrintRuc(s)
	
	resolve_modifier(p)

	if p.path:
		open_file(p)

	make_print(p)

	if p.path:
		close_file(p)

	return p