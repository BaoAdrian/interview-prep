# Data Structures
This directory contains various implementations of common data structures and their associated methods/functionality.

Data structures to be implemented
- Stack
- Queue
- Linked List
- Tree
- Graph
- Hash Table

# Getting Started
Each subdirectory for each data structure contains its own manual testing script and unittest suite that can be used to verify the behavior or functionality of the implemented data structure.

Alternatively, two handy scripts have been included to run ALL unittests (`exec_unittests.sh`) and run ALL manual/formatted output tests (`exec_ds_tests.sh`) and can be modified to include/remove flags depending on your desired usecase.

## Unittests
These tests are noted by the `unittest_<datastructure>.py` notation and utilize Python's standard libray, `unittest`, to provide basic automated testing of a data structures implementation. 

Example usage for the Binary Search Tree Data Structure:
```
$ python unittest_tree.py --help
usage: unittest_tree.py [-h] [-v] [-q] [--locals] [-f] [-c] [-b]
                        [-k TESTNAMEPATTERNS]
                        [tests [tests ...]]

positional arguments:
  tests                a list of any number of test modules, classes and test
                       methods.

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output
  -q, --quiet          Quiet output
  --locals             Show local variables in tracebacks
  -f, --failfast       Stop on first fail or error
  -c, --catch          Catch Ctrl-C and display results so far
  -b, --buffer         Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS  Only run tests which match the given substring

Examples:
  unittest_tree.py                           - run default set of tests
  unittest_tree.py MyTestSuite               - run suite 'MyTestSuite'
  unittest_tree.py MyTestCase.testSomething  - run MyTestCase.testSomething
  unittest_tree.py MyTestCase                - run all 'test*' test methods
                                       in MyTestCase
```

## Manual Testing Script
These manual tests are noted by the `test_<datastructure>.py` notation and support various command-line arguments to test specific aspects of the target data structure.

Example usage for the Binary Search Tree Data Structure:
```
$ python test_tree.py --help
usage: test_tree.py [-h] [--test-all] [--test-insert] [--test-remove]
                    [--test-find] [--test-traversals] [--test-height]

optional arguments:
  -h, --help         show this help message and exit
  --test-all         Test the functionality of ALL Tree methods
  --test-insert      Test the functionality of BSTNode.insert()
  --test-remove      Test the functionality of BSTNode.remove()
  --test-find        Test the functionality of BSTNode.search()
  --test-traversals  Test the functionality of the various BST traversals
  --test-height      Test the functionality of BSTNode.get_height()
```

If you wish to view all comprehensive tests being executed with their supported output, you can use the `--test-all` flag with any of the data structure scripts.
