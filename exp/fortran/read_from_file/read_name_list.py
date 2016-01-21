import os
open('a.tmp','w').write(
"""
&LIST
x = 1,
y = 2,
z = 3
/
"""
)

c = """
program a

integer :: u = 10

integer :: x, y ,z

open(u, file='a.tmp', status='old')

namelist /list/ x, y, z

read(u, list) 

close(u)

print *, x, y, z

end program
"""

open('a.f90','w').write(c)

os.system("""
ifort a.f90 -o a.b
./a.b
""")

