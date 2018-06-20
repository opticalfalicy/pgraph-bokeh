class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x = 0, y = 0)
        debug_vertex_2 = Vertex('t1', x = 0.7, y = 0.2)
        debug_vertex_3 = Vertex('t1', x = -0.4, y = 0.5)
        debug_vertex_4 = Vertex('t1', x = 0, y = 1)
        
        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)
        debug_edge_2 = Edge(debug_vertex_2)
        debug_vertex_3.edges.append(debug_edge_2)
        debug_edge_3 = Edge(debug_vertex_3)
        debug_vertex_4.edges.append(debug_edge_3)

        self.vertexes.extend([debug_vertex_1, debug_vertex_4, debug_vertex_2, debug_vertex_3])