# Graphs
This directory contains the Python implementation of the Graph Data Structure. Included are two testing scripts, `test_graph.py` and `unittest_graph.py` (see below for usages), that can be used to view/test the functionality of the implemented methods.

In addition to the provided test scripts, `word-ladder-problem.py` has been included to showcase the Graph DS usage to solve the famous [Word Ladder Problem](https://en.wikipedia.org/wiki/Word_ladder).

# Usage

## Manual Tests
These tests can be used to visualize various operations performed on the implemented Graph.
```
$ python3 test_graph.py --help
usage: test_graph.py [-h] [--test-all] [--test-add] [--test-bfs] [--test-dfs]

optional arguments:
  -h, --help  show this help message and exit
  --test-all  Runs all tests for the Graph's Functionality
  --test-add  Tests the functionality of Graph.add_edge() &
              Graph.add_all_edges()
  --test-bfs  Tests the functionality of the Graph's Breadth First Search
  --test-dfs  Tests the functionality of the Graph's Depth First Search
```

## Unittests
These can be run to ensure the functionality works as expected

(WIP)

## Word Ladder Problem
Included in this directory is a sample file of words (`default_word_ladder.txt`) in the required format. You may view the programs execution by running 
```
$ python3 word-ladder-problem.py --run-example
```

Once you become familiar with the expected format of the file/input, you may utilize the corresponding flags to provide your own puzzle with `src` and `dst` words to view its viability!
```
$ python3 word-ladder-problem.py --help
usage: word-ladder-problem.py [-h] [--run-example] [-f FILE] [-s SRC] [-d DST]

optional arguments:
  -h, --help            show this help message and exit
  --run-example         Runs sample iteration using provided file and SRC
                        (FOOL)/ DST(SAGE)
  -f FILE, --file FILE  Input file containing valid words used to build Graph
  -s SRC, --src SRC     Source KEY (word) to begin the ladder
  -d DST, --dst DST     Destionan KEY (word) to complete the ladder
```