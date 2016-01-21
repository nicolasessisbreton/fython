int i
real x(10)

for i in [1, 10]:
  x[i] = i
  print 'x({:i}) = {:x[i]}'

print .x_final 'x is {v:x}'

# string to specify the path
print './x_transformed.out' """
  x+10 is: {vc:x+10}
  x-10 is : {vc:x-10}
  """

# Yes, Python multiline string
