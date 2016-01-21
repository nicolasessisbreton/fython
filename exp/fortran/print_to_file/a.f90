
program a

integer :: u = 10

open(u, file='a.tmp', status='replace')

write(u, '(f6.2)') 100.5678


close(u)

end program
