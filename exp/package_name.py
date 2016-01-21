import inspect

f = inspect.currentframe()

print(f.f_globals)

x = inspect.getfile(f)
print(inspect.getmodulename(x))

print(inspect.getmodule(f).__name__)