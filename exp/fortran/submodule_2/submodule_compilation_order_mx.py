import os
c = """
rm -rf *.mod *.so *.o


ifort -shared -fpic mx.f90

"""

os.system(c)

# os.system('nm -D a.so')
