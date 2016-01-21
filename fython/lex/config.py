from ..config import *

leading_space_re = re.compile('\s*')

bofx = '<bofx>'
eofx = '<eofx>'

linefeedx = '<linefeedx{:d}>'
newlinex = '<newlinex>'

indentx = '<indentx>'
dedentx = '<dedentx>'

newlinex_mark = '<{:d}<newlinex>'

len_newlinex = len(newlinex)
pos_lineno_linefeedx = len('<linefeedx') 

def get_leading_space(s):
	return leading_space_re.findall(s)[0]