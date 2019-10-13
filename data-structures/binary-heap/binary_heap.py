"""
BinaryHeap: Implementation of the Binary Heap represented 
by a list of nodes given the maintainence of a complete 
binary tree.

O(logn) insertion and removal
"""
class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, node):
        """
        insert: Inserts a given node into the corresponding 
        position within the binary heap. 
        Runtime: O(logn)
        """
        self.heap_list.append(node)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, i):
        """
        percolate_up: Beginning at the given index, moves the 
        corresponding nodes up into its correct position within
        the heap to maintain/restore heap order property.
        """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def delete_min(self):
        """
        delete_min: Removes the root node (for a Priority Queue,
        the node with the current highest priority) and restores
        heap order & structure properties.
        Runtime: O(logn)
        """
        min_node = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop() # Remove the root node
        self.percolate_down(1)
        return min_node

    def percolate_down(self, i):
        """
        percolate_down: Beginning at the given index, moves 
        the corresponding node down into its correct posiion
        within the heap to maintain/restore heap order property.
        """
        while i * 2 <= self.size:
            mc_idx = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc_idx]:
                # Swap
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc_idx]
                self.heap_list[mc_idx] = temp
            i = mc_idx

    def min_child(self, i):
        """
        min_child: Find the node in the Binary Heap that 
        will be percolated up, swapping positions with its 
        parents. 
        This is a suboperation of the delete_min() call
        """
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def build_heap(self, nodes):
        """
        build_heap: Provided a list of nodes, creates a binary
        heap.
        Runtime: O(n)
        """
        self.size = len(nodes)
        i = len(nodes) // 2
        self.heap_list = [0] + nodes[:]
        while i > 0:
            self.percolate_down(i)
            i -= 1