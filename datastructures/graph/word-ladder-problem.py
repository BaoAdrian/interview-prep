"""
word_ladder_problem.py
This program is meant to show to how to solve the Word
Ladder Problem using the Graph Data Structure and BFS Algorithm.

Problem Description:
You are given a starting word, "FOOL" and your goal is to 
change that word into "SAGE". You can only modify a single 
letter at a time and each iteration must result in a valid
word. For example:

FOOL < Starting word
POOL
POLL
POLE
PALE
SALE
SAGE < Goal
"""
from graph import Graph, Vertex
import argparse    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-example', action='store_true',
                        help='Runs sample iteration using provided file and SRC (FOOL)/ DST(SAGE)')
    parser.add_argument('-f', '--file', default='default_word_ladder.txt',
                        help='Input file containing valid words used to build Graph')
    parser.add_argument('-s', '--src',
                        help='Source KEY (word) to begin the ladder')
    parser.add_argument('-d', '--dst',
                        help='Destionan KEY (word) to complete the ladder')
    args = parser.parse_args()
    return args

def print_ladder(src, dst, ladder):
    print("Utilizing: Source ({}) > Destination ({})".format(src, dst))
    print("Ladder from {} to {}".format(src, dst))
    print("> {} <".format('-'*len(src)))
    for step in ladder:
        print("> {} <".format(step))
    print("> {} <".format('-'*len(src)))

def run_example():
    graph = build_graph("default_word_ladder.txt")
    print("Generated Graph:\n{}".format(graph))
    src, dst = "FOOL", "SAGE"
    ladder = graph.bfs(src, dst)
    print_ladder(src, dst, ladder)

def run_custom(args):
    if not args.src or not args.dst:
        print("Error, src/dst words are required to solve this problem")
        exit(0)
    graph = build_graph(args.file)
    print("Generated Graph:\n{}".format(graph))
    ladder = graph.bfs(args.src, args.dst)
    print_ladder(args.src, args.dst, ladder)

def build_graph(filename):
    """
    build_graph: Each word can be broken down into subwords that
    include a space where a possible replacement can be made to
    test the new words viability. For example:
    TOOL can be broken down into: _OOL, T_OL, TO_L, and TOO_
    where each space represents an insertion point to test a new
    word.
    """
    d = {}
    graph = Graph()
    
    with open(filename, "r") as f:
        # Create buckets for words that differ by one letter
        for line in f:
            word = line.strip()
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket not in d:
                    d[bucket] = []
                d[bucket].append(word)
            
        # Add Vertices and Edges for wards in the same bucket
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        graph.add_edge(word1, word2)
    
    return graph

def main():
    args = parse_args()
    
    if args.run_example:
        run_example()
        exit(0)
    if args.file:
        run_custom(args)


if __name__ == "__main__":
    main()