import os
c = """
rm -rf *.mod *.so *.o

ifort m1.f90 -c -fpic 
ifort m2.f90 -c -fpic 
ifort m4.f90 -c -fpic 

ifort -shared -o a.so m1.o m2.o m4.o 

"""

os.system(c)

# os.system('nm -D a.so')
