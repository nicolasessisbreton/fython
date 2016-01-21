from ..printruc.printruc_type import PrintRuc
from ..printruc.resolve_modifier import resolve_modifier
from .open_file import open_file
from .make_read import make_read
from ..printruc.close_file import close_file

def readruc(s):
	p = PrintRuc(s)
	
	resolve_modifier(p)

	if p.path:
		open_file(p)

	make_read(p)

	if p.path:
		close_file(p)

	return p