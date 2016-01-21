int: x y z
int u(3)

print .data mode(w) '1, 2, 3' # explicitly creating a new file with the mode modifier

read .data: x y z

print 'x {:x}'
print 'y {:y}'
print 'z {:z}'

# vectors too
read .data u
print 'u is {v:u}'