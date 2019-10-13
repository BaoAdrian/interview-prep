# Tree
This directory contains the Python implementation of the Tree Data Structure. Included are two testing scripts, `test_tree.py` and `unittest_tree.py` (see below for usages), that can be used to view/test the functionality of the implemented methods.

# Usage

## Manual Tests
Run this script if you wish to visualize the functionality/various operations of the Tree Data Structure.
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

## Unittests
Run this script if you wish to verify the expected functionality of the Tree Data Structure.
```
$ python3 unittest_tree.py --help
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