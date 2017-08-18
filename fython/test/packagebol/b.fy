import asis type_provider(target_class=T)

def quicksort:
	T dimension(10) in x
	int: i r
	for i in [1, 10]:
		r = x[i].lt( x[i+1] )
		print 'i {:r}'