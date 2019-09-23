# Stack
This directory contains the Python implementation of the Stack Data Structure. Included are two testing scripts, `test_stack.py` and `unittest_stack.py` (see below for usages), that can be used to view/test the functionality of the implemented methods.

# Usage

## Manual Test
Run this script if you wish to visualize the functionality/various operations of the Stack Data Structure.
```
$ python test_stack.py --help
usage: test_stack.py [-h] [--test-all] [--test-push] [--test-pop]
                     [--test-peek] [--test-search]

optional arguments:
  -h, --help     show this help message and exit
  --test-all     Test the functionality of ALL Stack methods
  --test-push    Test the functionality of Stack.push()
  --test-pop     Test the functionality of Stack.pop()
  --test-peek    Test the functionality of Stack.peek()
  --test-search  Test the functionality of Stack.search() &
                 Stack.search_and_remove()
```

## Unittests
Run this script if you wish to verify the expected functionality of the Stack Data Structure.
```
usage: unittest_stack.py [-h] [-v] [-q] [--locals] [-f] [-c] [-b]
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
  unittest_stack.py                           - run default set of tests
  unittest_stack.py MyTestSuite               - run suite 'MyTestSuite'
  unittest_stack.py MyTestCase.testSomething  - run MyTestCase.testSomething
  unittest_stack.py MyTestCase                - run all 'test*' test methods
                                       in MyTestCase
```