class Graph(dict):
	def __init__(self, vs, es):
		"""
		Create a new graph. (vs) is the list of 
		vertices; (es) is the list of edges.
		"""
		for v in vs:
			self.add_vertex(v)
		for e in es:
			self.add_edge(e)

	def add_vertex(self, v):
		"""
		add (v) to graph
		"""
		self[v] = {}
	
	def add_edge(self, e):
		"""
		add (e) to the graph by adding and entry 
		in both directions.If there is already an 
		edge connecting these vertices, the new
		edge replaces it
		"""
		v, w = e
		self[v][w] = e
		self[w][v] = e

class Vertex(object):
	def __init__(self, label = ''):
		self.label = label
	
	def __repr__(self):
		return "Vertex(%s)" % repr(self.label)

	__str__ = __repr__


class Edge(tuple):
	def __new__(cls, *vs):
		return tuple.__new__(cls, vs)

	def __repr__(self):
		return "Edge(%s, %s)" % (repr(self[0]), repr(self[1]))
	__str__ = __repr__
	
