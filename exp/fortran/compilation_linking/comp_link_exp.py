import os

os.system('rm -rf *.o *.so *.mod *.smod *.f90')

def f(**kwargs):
	for key, code in kwargs.items():
		if key == 'cmd':
			continue

		open(key+'.f90', 'w').write(code)

	os.system(kwargs['cmd'])
f(
a = """
module a

end module
""",

b = """
module b
use a
end module
""",

c = """
submodule (b) c

end submodule
""",

cmd="""
ifort -c a.f90
ifort -c b.f90
ifort -c c.f90
ifort -shared -fpic -o out.so b.o
"""
)