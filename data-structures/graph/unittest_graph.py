from graph import Graph, Node
import unittest

def build_graph():
    graph = Graph()
    graph.add_all_edges(1, [3,6,7])
    graph.add_all_edges(2, [1,2])
    graph.add_all_edges(3, [2, 4])
    graph.add_all_edges(4, [5])
    graph.add_all_edges(5, [3,9])
    graph.add_all_edges(6, [6,7])
    graph.add_all_edges(7, [6,10])
    graph.add_all_edges(8, [9])
    graph.add_all_edges(9, [5,8])
    graph.add_all_edges(10, [10])
    return graph

class TestGraph(unittest.TestCase):
    def test_add_vertices(self):
        graph = Graph()
        graph.add_node(100)
        self.assertTrue(100 in graph)
        self.assertEqual(graph.size(), 1)
        graph.add_node(200)
        graph.add_node(300)
        self.assertTrue(200 in graph and 300 in graph)
        self.assertEqual(graph.size(), 3)

    def test_add_edge(self):
        graph = Graph()
        graph.add_edge(100, 200)
        self.assertTrue(100 in graph and 200 in graph)
        self.assertEqual(graph.size(), 2)
        connections = [node.get_id() for node in graph.get_node(100).get_neighbors()]
        self.assertEqual(connections, [200])
        graph.add_edge(100, 300)
        graph.add_edge(100, 400)
        graph.add_edge(300, 400)
        self.assertTrue(300 in graph and 400 in graph)
        self.assertEqual(graph.size(), 4)
        connections = [node.get_id() for node in graph.get_node(100).get_neighbors()]
        self.assertEqual(connections, [200, 300, 400])

    def test_add_all_edges(self):
        graph = Graph()
        self.assertEqual(graph.size(), 0)
        graph.add_all_edges(100, [200, 300, 400])
        graph.add_all_edges(200, [100, 300, 400])
        graph.add_all_edges(600, [500])
        self.assertTrue(100 in graph and 200 in graph and 300 in graph  \
            and 400 in graph and 500 in graph and 600 in graph)
        self.assertEqual(graph.size(), 6)
        connections = [node.get_id() for node in graph.get_node(200).get_neighbors()]
        self.assertEqual(connections, [100, 300, 400])

    def test_bfs(self):
        graph = build_graph()
        src, dst = 8, 6
        expected_res = [8, 9, 5, 3, 2, 1, 6]
        path = graph.bfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 10, 1
        expected_res = []
        path = graph.bfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 2,9
        expected_res = [2,1,3,4,5,9]
        path = graph.bfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 4,4
        expected_res = [4]
        path = graph.bfs(src, dst)
        self.assertEqual(expected_res, path)
        

    def test_iter_dfs(self):
        graph = build_graph()
        src, dst = 8, 6
        expected_res = [8, 9, 5, 3, 2, 1, 7, 6]
        path = graph.dfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 10, 1
        expected_res = []
        path = graph.dfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 2,10
        expected_res = [2,1,7,10]
        path = graph.dfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 4,4
        expected_res = [4]
        path = graph.dfs(src, dst)
        self.assertEqual(expected_res, path)

    def test_recur_dfs(self):
        graph = build_graph()
        src, dst = 8, 6
        expected_res = [8, 9, 5, 3, 2, 1, 6]
        path = graph.recursive_dfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 10, 1
        expected_res = []
        path = graph.recursive_dfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 2,10
        expected_res = [2,1,6,7,10]
        path = graph.recursive_dfs(src, dst)
        self.assertEqual(expected_res, path)
        graph.refresh()
        src,dst = 4,4
        expected_res = [4]
        path = graph.recursive_dfs(src, dst)
        self.assertEqual(expected_res, path)

if __name__ == "__main__":
    unittest.main()
