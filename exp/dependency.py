import networkx as nx

t = nx.DiGraph()

t.add_edge(2, 1)
t.add_edge(3, 1)
t.add_edge(4, 3)


print(
	nx.topological_sort(t)
)

class A:
	def __init__(s, a):
		s.a = a

	def __hash__(s):
		return hash(s.a)

	def __eq__(s, other):
		return s.a == other.a

	def __repr__(s):
		return str(s.a)



a = A(1)
b = A(2)
c = A(3)

t = nx.DiGraph()
t.add_edge(b, a)
t.add_edge(c, b)

print(
	nx.topological_sort(t)
)