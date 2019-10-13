# Linked List
This directory contains the Python implementation of the Linked List Data Structure. Included are two testing scripts, `test_stack.py` and `unittest_stack.py` (see below for usages), that can be used to view/test the functionality of the implemented methods.

# Usage

## Manual Test
Run this script if you wish to visualize the functionality/various operations of the Linked List Data Structure.
```
$ python test_linkedlist.py --help
usage: test_linkedlist.py [-h] [--test-all] [--test-add] [--test-removal]
                          [--test-search]

optional arguments:
  -h, --help      show this help message and exit
  --test-all      Test the functionality of ALL LinkedList methods
  --test-add      Test the functionality of the various methods used to add
                  Nodes to the LinkedList (add, append, insert)
  --test-removal  Test the functionality of the various node removal methods
                  of a LinkedList (remove_by_element, remove_by_index)
  --test-search   Test the functionality of LinkedList.search(target)
```

## Unittests
Run this script if you wish to verify the expected functionality of the Linked List Data Structure.
```
$ python3 unittest_linkedlist.py --help
usage: unittest_linkedlist.py [-h] [-v] [-q] [--locals] [-f] [-c] [-b]
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
  unittest_linkedlist.py                           - run default set of tests
  unittest_linkedlist.py MyTestSuite               - run suite 'MyTestSuite'
  unittest_linkedlist.py MyTestCase.testSomething  - run MyTestCase.testSomething
  unittest_linkedlist.py MyTestCase                - run all 'test*' test methods
                                       in MyTestCase
```