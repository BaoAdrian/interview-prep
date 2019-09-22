
class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
    
    def __contains__(self, id):
        return id in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, vertex_key):
        self.num_vertices += 1
        new_vertex = Vertex(vertex_key)
        self.vertices[vertex_key] = new_vertex
        return new_vertex
    
    def get_vertex(self, vertex_key):
        return self.vertices[vertex_key] if vertex_key in self.vertices else None

    def add_edge(self, src, dest, cost = 0):
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[src].add_neighbor(self.vertices[dest], cost)

    def get_vertices(self):
        return self.vertices.keys()

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connected_to = {}

    def __str__(self):
        return "{} > {}".format(str(self.id), str([vert.id for vert in self.connected_to]))

    def add_neighbor(self, neighbor, weight = 0):
        self.connected_to[neighbor] = weight
    
    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]