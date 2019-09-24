import argparse
from graph import Graph

def test_add():
    print_header(" Testing all methods of adding nodes/edges ")
    graph = Graph()
    print("Initial Graph: {}".format(graph))
    print("Adding a few nodes using graph.add_vertex(key)")
    graph.add_vertex(100)
    graph.add_vertex(200)
    graph.add_vertex(300)
    print("Graph: {}".format(graph))

    print("Now lets connect some nodes with Graph.add_edges(src, dst)")
    graph.add_edge(100, 200)
    graph.add_edge(100, 300)
    graph.add_edge(200, 100)
    graph.add_edge(300, 300)
    print("Graph: {}".format(graph))

    print("Now we can combine this effort using Graph.add_all_edges(src, dest_nodes)")
    graph.add_all_edges(500, [100, 200, 300])
    graph.add_all_edges(600, [500])
    graph.add_all_edges(700, [500, 600])
    print("Graph: {}".format(graph))

def test_bfs():
    print_header(" Testing Graph.bfs(src, dst) ")
    graph = build_graph()
    print("Graph:{}".format(graph))

    src, dst = 8, 6 # Path exists
    print("Path from {} to {} > {}".format(src, dst, graph.bfs(src,dst)))
    graph.refresh()
    src, dst = 10, 1 # Non-existent path
    print("Path from {} to {} > {}".format(src, dst, graph.bfs(src,dst)))
    graph.refresh()
    src, dst = 4,4 # Self
    print("Path from {} to {} > {}".format(src, dst, graph.bfs(src,dst)))


def test_dfs():
    print_header(" Testing Graph.dfs(src, dst) ")
    graph = build_graph()
    print("Graph:{}".format(graph))
    src, dst = 8, 6 # Path exists
    print("Path from {} to {} > {}".format(src, dst, graph.dfs(src,dst)))
    graph.refresh()
    src, dst = 10, 1 # Non-existent path
    print("Path from {} to {} > {}".format(src, dst, graph.dfs(src,dst)))
    graph.refresh()
    src, dst = 4,4 # Self
    print("Path from {} to {} > {}".format(src, dst, graph.dfs(src,dst)))

def test_dfs_recursive():
    print_header(" Testing Graph.recursive_dfs(src, dst) ")
    graph = build_graph()
    print("Graph:{}".format(graph))
    src, dst = 8, 6 # Path exists
    print("Path from {} to {} > {}".format(src, dst, graph.recursive_dfs(src,dst)))
    graph.refresh()
    src, dst = 10, 1 # Non-existent path
    print("Path from {} to {} > {}".format(src, dst, graph.recursive_dfs(src,dst)))
    graph.refresh()
    src, dst = 4,4 # Self
    print("Path from {} to {} > {}".format(src, dst, graph.recursive_dfs(src,dst)))

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

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-all', action='store_true',
                        help='Runs all tests for the Graph\'s Functionality')
    parser.add_argument('--test-add', action='store_true',
                        help='Tests the functionality of Graph.add_edge() & Graph.add_all_edges()')
    parser.add_argument('--test-bfs', action='store_true',
                        help='Tests the functionality of the Graph\'s Breadth First Search')
    parser.add_argument('--test-dfs', action='store_true',
                        help='Tests the functionality of the Graph\'s Depth First Search')
    args = parser.parse_args()
    return args

def print_header(msg):
    """
    print_header: Utility function to print headers.
    """
    SPACING = 60
    print("\n" + "-"*SPACING)
    print(msg.center(SPACING, "-"))
    print("-"*SPACING)

def main():
    args = parse_args()
    
    if args.test_all or args.test_add:
        test_add()
    if args.test_all or args.test_bfs:
        test_bfs()
    if args.test_all or args.test_dfs:
        test_dfs()
        test_dfs_recursive()

if __name__ == "__main__":
    main()
