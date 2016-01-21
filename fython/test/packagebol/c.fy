import .a(*)

import .b(*)
|| 
	type_provider = .a
	target_class = A 
||

A dimension(10) a
int i

for i in [1, 10]:
	a.x = i

quicksort(a)