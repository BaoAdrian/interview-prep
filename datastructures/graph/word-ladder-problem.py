"""
word_ladder_problem.py
This program is meant to show to how to solve the Word
Ladder Problem (invented in 1878 by Lewis Carroll) using
the Graph Data Structure and BFS Algorithm.

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
from interview-prep.Data-Structures.queue import *
from graph import *
import argparse

class VertexExtended(Vertex):
    def __init__(self, id):
        super().__init__(id)
        self.distance = None
        self.predecessor = None
        self.color = 'white'

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_predecessor(self):
        return self.predecessor

    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='default_word_ladder.txt',
                        help='Input file containing valid words used to build Graph')
    args = parser.parse_args()
    return args

def build_graph(args):
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
    infile = open(args.file, "r")

    # Create buckets for words that differ by one letter
    for line in infile:
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
        
def bfs(graph, start_vertex):
    """
    bfs: start > VertexExtended
    """
    start_vertex.set_distance(0)
    start_vertex.set_predecessor(None)
    vertex_queue = Queue()
    vertex_queue.enqueue(start_vertex)

def main():
    args = parse_args()
    build_graph(args)


if __name__ == "__main__":
    main()