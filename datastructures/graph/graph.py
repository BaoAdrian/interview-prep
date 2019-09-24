"""
Graph: This class implements the Graph data structure
and its assoicated methods. The Graph is represented by 
a map of { ID : Vertex Object } pairs.
"""

from queue import Queue

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        
    def __contains__(self, id):
        return id in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        string = "{\n"
        for k, v in self.vertices.items():
            string += "{} : {}\n".format(k, v)
        string += "}\n"
        return string

    def size(self):
        return self.num_vertices

    def add_vertex(self, vertex_key):
        """
        add_vertex: Given a vertex key, creates Vertex object 
        and adds to adjency list.
        """
        self.num_vertices += 1
        new_vertex = Vertex(vertex_key)
        self.vertices[vertex_key] = new_vertex
        return new_vertex
    
    def get_vertex(self, vertex_key):
        return self.vertices[vertex_key] if vertex_key in self.vertices else None

    def add_all_edges(self, src, dest_vertices):
        for dest in dest_vertices:
            self.add_edge(src, dest)

    def add_edge(self, src, dest):
        """
        add_edge: Adds edge from src to dest keys. If no 
        vertices exist with given src/dest keys, this function
        will create new vertices and connect them as neighbors.
        """
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[src].add_neighbor(self.vertices[dest])

    def get_vertices(self):
        return self.vertices.values()

    def backtrace(self, parent, src, dst):
        """
        backtrace: Trace back steps to generate a list of ordered
        steps from src to dst nodes within the graph. If dst node
        does not exist within the parent map, no path was found and
        return empty list. Otherwise, return backtracted list.
        """
        if dst not in parent:
            return []
        path = [dst]
        while path[-1] != src:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    def bfs(self, src, dst):
        """
        bfs: Standard breadth first search implementation
        that returns the shortest path, if exists, from src
        to dst vertex in the graph. If no path exists, returns
        empty list.
        Runtime: O(V+E)
        """
        if src == dst:
            # Search not required when target is self
            return [src]
        parent = {} # Keep track of parents in path if found
        start = self.get_vertex(src)
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            curr = queue.get()
            if curr.get_id() == dst:
                return self.backtrace(parent, src, dst)
            for neighbor in curr.get_connections():
                if neighbor.get_visited() == False:
                    parent[neighbor.get_id()] = curr.get_id()
                    neighbor.set_visited(True)
                    queue.put(neighbor)
        return []

    def dfs(self, src, dst):
        """
        dfs: Iterative Depth First Search implementation that 
        traverses graph searching for a path from src to dst. 
        If found, returns its path, otherwise, returns empty list
        Runtime: O(V+E)
        """
        stack = [(src, [src])]
        while stack:
            (key, path) = stack.pop()
            vertex = self.get_vertex(key)
            if vertex.get_visited() == False:
                vertex.set_visited(True)
                if key == dst:
                    return path
                for neighbor in self.vertices[key].get_connections():
                    stack.append((neighbor.get_id(), path + [neighbor.get_id()]))
        return []

    def recursive_dfs(self, src, dst):
        """
        recursive_dfs: Recursive implementation of a Depth First Search
        given start and end points. Uses helper funciton to  keep track 
        of the current path by maintaing a map of parents through the 
        recursive stack. 
        If path is found, map is returned. Otherwise, returns None

        NOTE: In some cases, returned path from recursive vs iterative 
        dfs may differ due to order of processing for vertices.
        """
        parents = self.recur_dfs_helper(src, dst, {})
        return self.backtrace(parents, src, dst)

    def recur_dfs_helper(self, src, dst, parents):
        """
        recur_dfs_helper: Helper function used to maintain path from
        src to dst (if one exists).
        """
        for neighbor in self.vertices[src].get_connections():
            if not neighbor.get_visited():
                neighbor.set_visited(True)
                parents[neighbor.get_id()] = src
                self.recur_dfs_helper(neighbor.get_id(), dst, parents)
        return parents

    def refresh(self):
        """ Refreshes all visited nodes to vanilla """
        for vertex in self.get_vertices():
            vertex.set_visited(False)

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connected_to = []
        self.visited = False # Protect against cycles in search algorithms

    def __str__(self):
        return "{} > {}".format(str(self.id), str([vert.id for vert in self.connected_to]))

    def add_neighbor(self, neighbor):
        self.connected_to.append(neighbor)
    
    def get_connections(self):
        return self.connected_to

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_visited(self):
        return self.visited

    def set_visited(self, boolean):
        self.visited = boolean