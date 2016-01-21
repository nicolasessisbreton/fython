import os
open('a.tmp','w').write(
"""
1, 10, 20
2
3
"""
)

c = """
program a

integer :: u = 10

integer :: x, y ,z

open(u, file='a.tmp', status='old')

read(u, *) x
read(u, *) y
read(u, *) z

close(u)

print *, x, y, z

end program
"""

open('a.f90','w').write(c)

os.system("""
ifort a.f90 -o a.b
./a.b
""")

