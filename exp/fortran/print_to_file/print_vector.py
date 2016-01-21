import os
c = """
program a

integer :: u = 10

integer, dimension(1e3) :: x = 2

open(u, file='a.tmp', status='replace')

write(u, '(a, *(g0), a, (g0), a)') 'a', x, 'b', x, 'c'

write(u, "(*(g0,:', '))") x


close(u)

end program
"""

open('a.f90','w').write(c)

os.system("""
ifort a.f90 -o a.b
./a.b
""")

print(open('a.tmp', 'r').read())
