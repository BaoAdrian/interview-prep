"""
Graph: This class implements the Graph data structure
and its assoicated methods. The Graph is represented by 
a map of { ID : Vertex Object } pairs.
"""

from queue import Queue

class Graph:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0
        
    def __contains__(self, id):
        return id in self.nodes

    def __iter__(self):
        return iter(self.nodes.values())

    def __str__(self):
        string = "{\n"
        for k, v in self.nodes.items():
            string += "{} : {}\n".format(k, v)
        string += "}\n"
        return string

    def size(self):
        return self.num_nodes

    def add_node(self, node_id):
        """
        add_vertex: Given a vertex key, creates Vertex object 
        and adds to adjency list.
        """
        self.num_nodes += 1
        new_vertex = Node(node_id)
        self.nodes[node_id] = new_vertex
        return new_vertex
    
    def get_node(self, node_id):
        return self.nodes[node_id] if node_id in self.nodes else None

    def add_all_edges(self, src, dest_vertices):
        for dest in dest_vertices:
            self.add_edge(src, dest)

    def add_edge(self, src, dest):
        """
        add_edge: Adds edge from src to dest keys. If no 
        vertices exist with given src/dest keys, this function
        will create new vertices and connect them as neighbors.
        """
        if src not in self.nodes:
            self.add_node(src)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[src].add_neighbor(self.nodes[dest])

    def get_nodes(self):
        return self.nodes.values()

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
        start = self.get_node(src)
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            curr = queue.get()
            if curr.get_id() == dst:
                return self.backtrace(parent, src, dst)
            for neighbor in curr.get_neighbors():
                if neighbor.is_visited() == False:
                    parent[neighbor.get_id()] = curr.get_id()
                    neighbor.visit()
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
            node = self.get_node(key)
            if node.is_visited() == False:
                node.visit()
                if key == dst:
                    return path
                for neighbor in self.nodes[key].get_neighbors():
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
        for neighbor in self.nodes[src].get_neighbors():
            if not neighbor.is_visited():
                neighbor.visit()
                parents[neighbor.get_id()] = src
                self.recur_dfs_helper(neighbor.get_id(), dst, parents)
        return parents

    def refresh(self):
        """ Refreshes all visited nodes to vanilla """
        for node in self.get_nodes():
            node.unvisit()

class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False # Protect against cycles in search algorithms

    def __str__(self):
        return "{} > {}".format(str(self.id), str([vert.id for vert in self.neighbors]))

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def get_neighbors(self):
        return self.neighbors

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def visit(self):
        self.visited = True

    def unvisit(self):
        self.visited = False
    
    def is_visited(self):
        return self.visited