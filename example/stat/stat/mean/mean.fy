real cons boltzman = 10 # a constant

int plank = 8 # a global variable

def cube_mean:
  real in: x y z
  real out r

  r = x + y + z
  r /= 3 
  r **= 3

  ## 
    Yes, Fython has all the augmented assignment operators (+=, -=, *=, /=, **=).
    Yes, this is a multiline comment.
  ## 

def moving_mean:
  int in n 
  real inout x(n)
  int i 

  # let's forget about the edges
  for i in [2, n-1]:
    x[i] = sum( x[i-1:i+1] ) / 3

  if x[1] > 5:
    print 'x[1] is bigger than 5: x[1]={:x[1]}'
    print """
      All the values in x are:  
      {v:x}
    """

  ## 
    The Python vector x will be modified in-place.

    The print format mini-language is that of Python, plus a few additions.
    The v directive eases the printing of vector.

  ## 

def string_mean:
  char(3) in x(3)
  real out r
  int: i j 

  # a mean on strings? creative.
  for i in [1, 3]:
    for j in [1, 3]:
      r += ichar( x[i][j:j] )

  r /= 10

  r += boltzman + plank # essential constants for any calculation, aren't they?

  ##
    The ichar function gives the ascii code of a character.

    The ichar function is an intrinsic Fortran function.
    Yes, you have access to all of them.
  ##

