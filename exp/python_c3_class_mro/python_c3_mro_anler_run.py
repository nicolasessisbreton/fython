import itertools

cls = 'd'
mro_lists = [ ['d', 'c'], ['c', 'b'], ['b', 'a'], ['a', 'o'] ]

# Make a copy so we don't change existing content
mro_lists = [list(mro_list[:]) for mro_list in mro_lists]
print(1, mro_lists)

# Set up the new MRO with the class itself
mro = []
print(2, cls)

# The real algorithm goes here
while True:
	# Reset for the next round of tests
	candidate_found = False
	
	for mro_list in mro_lists:
		print(3, mro_list)
		if not len(mro_list):
			# Any empty lists are of no use to the algorithm
			continue
			
		# Get the first item as a potential candidate for the MRO
		candidate = mro_list[0]
		
		if candidate_found:
			# Candidates promoted to the MRO are no longer of use
			if candidate in mro:
				mro_list.pop(0)
			# Don't bother checking any more candidates if one was found
			continue
		
		# See if it's in any position other than fist in any of the other lists
		print(4, list(itertools.chain(*(x[1:] for x in mro_lists))))
		if candidate in itertools.chain(*(x[1:] for x in mro_lists)):
			# Isn't a valid candidate yet and we need to move on to the first class
			# in the next list
			continue
		else:
			# The candidate is valid and should be promoted to the MRO
			mro.append(candidate)
			mro_list.pop(0)
			candidate_found = True
	if not sum(len(mro_list) for mro_list in mro_lists):
		# There are no MROs to cycle through, so we're all done
		break
	
	if not candidate_found:
		# No valid candidate was available, so we have to bail out
		raise TypeError("Inconsistent MRO")

print(mro)

