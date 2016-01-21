import re

def csv_replace_fct(s):
	s = re.sub('\s', '', s)
	s = re.sub('^.*?=', '', s)
	s = re.sub(',.*?=', ',', s)
	return s

