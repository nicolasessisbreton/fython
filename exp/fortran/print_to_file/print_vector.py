import os
c = """
program a

integer :: u = 10

integer, dimension(3) :: x = 2

open(u, file='a.tmp', status='replace')

! write(u, '(a, *(g0), a, (g0), a)') 'a', x, 'b', x, 'c'

! write(u, "(a, (3(g0,', '),'null'), a, 3(g0), a)") 'a', x, 'b', x, 'c'

write(u, "(a, 3(g0,', '), tl2, a)") 'a', x, 'b'

! write(u, "(3(g0,:,', '))") x

! write(u, "(*(g0,:', '))") x


close(u)

end program
"""

open('a.f90','w').write(c)

os.system("""
ifort a.f90 -o a.b
./a.b
""")

print(open('a.tmp', 'r').read())
