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

	def get_edge(self, v, w):
		try:
			return self[v][w]
		except KeyError:
			return None
	
	def remove_edge(self, e):
		for k in self.keys():
			for k2, v2 in self[k].items():
				if v2 == e:
					del self[k]
	
	def vertices(self):
		return self.keys()

	def edges(self):
		es = []
		for k in self.keys():
			for k2, v2 in self[k].items():
				if v2 not in es:
					es.append(v2)
		return es

	def out_vertices(self, v):
		return self[v].keys()

	def out_edge(self, v):
		return self[v].values()


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
	
def add_all_edges(g):
	for v in g.vertices():
		for w in g.vertices():
			if v != w:
				g.add_edge(Edge(v,w))





if __name__ == "__main__":
	v = Vertex('v')
	w = Vertex('w')
	x = Vertex('x')
	y = Vertex('y')
	g = Graph([v, w, x, y], [] )
	print g
	add_all_edges(g)
	print g



