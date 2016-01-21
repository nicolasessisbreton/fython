class Magnetism:
  real maxwell = 8
  real pointer tesla(:) => null()
  real allocatable bohr(:)

  def energy:
    self in # first argument is always self
    real res r
    r = self.maxwell + sum(self.tesla)
      
  def pget courant:
    self in
    real res r
    r = self.maxwell + sum(self.bohr)

  def pset courant:
    s inout # any name is allow for the self argument
    real in value
    s.bohr = value

real target x(10) = 1
Magnetism m

m.tesla => x # pointer assignment
print 'energy {:m.energy()}'

# happy allocation
alloc m.bohr(8) 
print 'bohr {v:m.bohr}'

# getter/setter
m.courant = 4.
print 'courant {:m.courant}'

# happy deallocation
dealloc m.bohr
