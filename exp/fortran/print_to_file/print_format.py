import os
c = """
program a

integer :: u = 10

open(u, file='a.tmp', status='replace')

write(u, '(f6.2)') 100.5678


close(u)

end program
"""

open('a.f90','w').write(c)

os.system("""
ifort a.f90 -o a.b
./a.b
""")

print(open('a.tmp', 'r').read())
