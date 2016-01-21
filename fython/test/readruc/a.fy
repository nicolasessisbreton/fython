char(10): variable_name='./file.out'
int: x y z(2, 2) 
int: variable_without_dot any_variable

# dotted
# assumes file extension is '.out'
read .file x
read url(.file) x

# path
read './file.out' x
read path('./file.out') x
read path(variable_name) x

open(unit=10, file='./file.out')
variable_without_dot = 10
any_variable = 10

read 10 x # number
read variable_without_dot x
read unit(any_variable) x

read .file x
read .file : x y z
read .file:
	x
	y
	z[:, 1]