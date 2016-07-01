from ..config import *
from .printruc import printruc 

def xipruc(linecod):
	s = linecod

	if s.debug:
		printruc(s)