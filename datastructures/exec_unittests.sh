#!/bin/bash

echo -e "\n==========================="
echo -e "Running Unit Test for Stack"
echo -e "===========================\n"
python3 ./stack/unittest_stack.py --verbose

echo -e "\n==========================="
echo -e "Running Unit Test for Queue"
echo -e "===========================\n"
python3 ./queue/unittest_queue.py --verbose

echo -e "\n=================================="
echo -e "Running Unit Test for Linked List"
echo -e "==================================\n"
python3 ./linked-list/unittest_linkedlist.py --verbose

echo -e "\n========================================="
echo -e "Running Unit Test for Binary Search Tree"
echo -e "=========================================\n"
python3 ./tree/unittest_tree.py --verbose
