# Graph Problems
This directory contains general graph problems not found on Leetcode, HackerRank, or CTCI.

## Word Ladder Problem
Included in this directory is a sample file of words (`default_word_ladder.txt`) in the required format. You may view a sample of the programs execution by running:
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