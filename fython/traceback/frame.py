from ..config import *

init = "\ncall <fytbk_init_frame>('{:s}:{:s}')\n"
delete = '\ncall <fytbk_del_frame>()\n'

def init_frame(module_url, routine_name):
	r = init.format(module_url, routine_name)
	return r

def del_frame():
	return delete
