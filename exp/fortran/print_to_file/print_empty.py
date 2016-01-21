import os
c = """
program a

integer :: u = 10

open(u, file='a.tmp', status='replace')

write(u, '()') 

close(u)

end program
"""

open('a.f90','w').write(c)

os.system("""
ifort a.f90 -o a.b
./a.b
""")

print(open('a.tmp', 'r').read())
