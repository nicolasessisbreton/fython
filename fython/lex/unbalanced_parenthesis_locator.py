def find(s, left, right):
	stack = []
	parentheses_locs = {}
	n = 1
	p = 0
	for i, c in enumerate(s):
		if c=='\n':
			n += 1
			p = 0
		x = i-p+1
		
		if c == left:
			stack.append((n,x))
			# if verbose: print(' '*len(stack), c, n, x)

		elif c == right:
			# if verbose: print(' '*len(stack), c, n, x)

			try:
				parentheses_locs[stack.pop()] = (n,x)
			except:
				return ['{}{}:too many close parentheses at line {} index {}'.format(left,right,n,x)]
	if stack:
		return ['{}{}:no matching close parenthesis to open parenthesis at line {} index {}'.format(left,right,*stack.pop())]

	return []

def find_unbalanced_parenthesis(s):
	r = []
	r += find(s, '(', ')')
	r += find(s, '[', ']')
	r += find(s, '{', '}')
	return '\n'.join(r)