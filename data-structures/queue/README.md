# Queue
This directory contains the Python implementation of the Queue Data Structure. Included are two testing scripts, `test_queue.py` and `unittest_queue.py` (see below for usages), that can be used to view/test the functionality of the implemented methods.

# Usage

## Manual Tests
Run this script if you wish to visualize the functionality/various operations of the Queue Data Structure.
```
$ python test_queue.py --help
usage: test_queue.py [-h] [--test-all] [--test-enqueue] [--test-dequeue]
                     [--test-peek] [--test-remove]

optional arguments:
  -h, --help      show this help message and exit
  --test-all      Test the functionality of ALL Queue methods
  --test-enqueue  Test the functionality of Queue.enqueue()
  --test-dequeue  Test the functionality of Queue.dequeue()
  --test-peek     Test the functionality of Queue.peek()
  --test-remove   Test the functionality of Queue.remove()
```

## Unittests
Run this script if you wish to verify the expected functionality of the Queue Data Structure.
```
$ python3 unittest_queue.py --help
usage: unittest_queue.py [-h] [-v] [-q] [--locals] [-f] [-c] [-b]
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
  unittest_queue.py                           - run default set of tests
  unittest_queue.py MyTestSuite               - run suite 'MyTestSuite'
  unittest_queue.py MyTestCase.testSomething  - run MyTestCase.testSomething
  unittest_queue.py MyTestCase                - run all 'test*' test methods
                                       in MyTestCase
```