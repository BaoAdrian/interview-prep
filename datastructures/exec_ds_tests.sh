#!/bin/bash

echo -e "\n\n=============================================="
echo -e "=============================================="
echo -e "\t\tRunning Manual Tests for Stack"
echo -e "=============================================="
echo -e "==============================================\n"
python3 ./stack/test_stack.py --test-all

echo -e "\n\n=============================================="
echo -e "=============================================="
echo -e "\t\tRunning Manual Tests for Queue"
echo -e "=============================================="
echo -e "==============================================\n"
python3 ./queue/test_queue.py --test-all

echo -e "\n\n=============================================="
echo -e "=============================================="
echo -e "\tRunning Manual Tests for Linked List"
echo -e "=============================================="
echo -e "==============================================\n"
python3 ./linked-list/test_linkedlist.py --test-all

echo -e "\n\n=============================================="
echo -e "=============================================="
echo -e " Running Manual Tests for Binary Search Tree"
echo -e "=============================================="
echo -e "==============================================\n"
python3 ./tree/test_tree.py --test-all
