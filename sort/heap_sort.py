#!/usr/bin/env python3
# coding: utf-8

import unittest
import random
from typing import List
import numpy as np


class MinHeap:
    """
    Implements a min-heap: each parent is less than or equal to its children
    Only functionality required for sorting is implemented.
    """
    def __init__(self, arr: List):
        # Copy an array
        self.arr = list(arr)
        # print("Starting building a heap")
        # Make a heap from the array
        self.build_heap()

    def build_heap(self):
        """
        Regroup elements in the array so that they form a heap.
        Must work in O(n) time
        """
        for i in range(len(self.arr)//2, 0, -1):
            # print("This is for {}th node".format(i))
            self.sift_down(i)

    def extract_min(self):
        """
        Returns the smallest value in the heap. Removes the element and rebuild a heap.
        Must work in O(log n) time
        """

        MIN = self.arr.pop(0)
        self.build_heap()
        return(MIN)

    def sift_down(self, node : int):
        """
        If the node (parent) value is greater than its children values (i.e. it violates the heap property),
        move it down until it finds its position.
        Must work in O(log n) time
        """

        def violated(left, right):
            ''' Helper Function : checking if the heap is violated.'''
            try:
                # checks if the children are bigger
                # if there is no children for this node, exception will take handle of the IndexError
                return self.arr[node-1] > self.arr[left-1] or self.arr[node-1] > self.arr[right-1]
                
            except:
                # Instead of IndexError, it will return False.
                return False
        
        def min_of_child(left, right):
            # checking if right exists
            if self.right(node) <= len(self.arr):
                # compare the left and right and return the minimum.
                return left if self.arr[left-1] <= self.arr[right-1] else right

            return left

        count = 0
        while node  > 0 and violated(self.left(node), self.right(node)):
            # print("Before node : ", node)
            count += 1
            child = min_of_child(self.left(node), self.right(node))
            # print(child)
            self.arr[child-1], self.arr[node-1] = self.arr[node-1], self.arr[child-1]
            node = self.parent(node)
            # print("After node : ", node)
            # print("For count {}: {}".format(count, self.arr))

        # print("Sift down ended")
        return(self.arr)
            
    @staticmethod
    def parent(node: int) -> int:
        return( node // 2)

    @staticmethod
    def left(node: int) -> int:
        return( node * 2)

    @staticmethod
    def right(node: int) -> int:
        return( node * 2 +1)


def heap_sort(arr: List):
    """ Sort the array using MinHeap. Must work in O(n log n) time """
    min_heap = MinHeap(arr)

    return([min_heap.extract_min() for i in range(len(arr))])

class Tests(unittest.TestCase):
    def array_testing(self, arr):
        expected = sorted(arr)
        result = heap_sort(arr)
        self.assertEqual(result, expected)

    def test_small(self):
        self.array_testing([1,3,4,2])

    def test_random(self):
        self.array_testing(list(np.random.randint(1, 50, 100)))

    # def test_big_random(self):
    #     self.array_testing(list(np.random.randint(int(-1e2), int(1e2), int(1e3))))
    
    # def test_larger_random(self):
    #     self.array_testing(list(np.random.randint(int(-1e2), int(1e2), int(1e5))))

    # def test_largest_random(self):
    #     self.array_testing(list(np.random.randint(int(-1e3), int(1e3), int(1e6))))

    # def test_empty(self):
    #     self.array_testing([])

    # def test_repeat(self):
    #     self.array_testing(list([3, 3, 3, 2, 2, 2, 4, 4, 5]))

if __name__ == '__main__':
    unittest.main()
    # x = MinHeap([5,4,2,1,3,2])
    # print(x.arr)