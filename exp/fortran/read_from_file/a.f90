
program a

integer :: u = 10

integer :: x, y ,z

open(u, file='a.tmp', status='old')

namelist /list/ x, y, z

read(u, list) 

close(u)

print *, x, y, z

end program
