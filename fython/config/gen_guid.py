from ..config import *
from string import ascii_lowercase as letters
from random import choice
from uuid import uuid4

def gen_guid():
	g = str(uuid4())

	g = g.replace('-', '')
	g = g[:guid_length-1]
	
	g = choice(letters) + g

	return g
