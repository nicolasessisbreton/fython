import os
from fython import *

writer("""
.ritchie.f90
  module ritchie
    real, bind(c) :: c = 10

    contains

      subroutine compile() bind(c)
        write(*, *) 'c is ', c
      end subroutine

  end module

.backus.fy
  import .ritchie(*)

  c = 20

  compile()
""")

os.system('gfortran ritchie.f90 -shared -fpic -o ritchie.so')

load('.backus')