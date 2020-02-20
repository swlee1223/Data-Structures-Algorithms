#!/usr/bin/env python3
# coding: utf-8

import unittest
import numpy as np
import random


class Tests(unittest.TestCase):
    def array_testing(self, arr):
        expected = list(sorted(arr))
        result = list(quick_sort(arr, 0, len(arr)-1))
        self.assertEqual(result, expected)

    def test_small(self):
        self.array_testing([1,3,4,2])

    def test_random(self):
        self.array_testing(np.random.randint(1, 50, 100))

    def test_big_random(self):
        self.array_testing(np.random.randint(int(-1e2), int(1e2), int(1e3)))
    
    def test_larger_random(self):
        self.array_testing(np.random.randint(int(-1e2), int(1e2), int(1e5)))

    def test_largest_random(self):
        self.array_testing(np.random.randint(int(-1e3), int(1e3), int(1e6)))

    def test_empty(self):
        self.array_testing([])

    def test_repeat(self):
        self.array_testing([3, 3, 3, 2, 2, 2, 4, 4, 5])

    
def partition(arr, l, r):
    '''This helper function is for quick sort.
    It sorts an array which given a pivot (this implementation, we are using a[r]), elements on its left to be smaller and to the right to be bigger

    Args: arr => input array
          l => starting position (including)
          r => end position (excluding)

    Returns: index i+1 which the element in that position is in the correct place.
    '''
    
    pivot = arr[r]
    # i is the index where the elements are smaller than the pivot.
    # e.g. If i =3, from index 0 to 3, the corresponding elements in the array are smaller than the pivot.

    
    i = l-1
    # for one pass
    for j in range(l,r):
        # finding position for the pivot
        # it increments s1 by 1 when the pivot is larger than current j
        if arr[j] <= pivot:
            i += 1

            # swap the current j element with i
            arr[i], arr[j] = arr[j], arr[i]

    # put s1 into the correct position

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return(i+1)

def quick_sort(arr, l, r):
    ''' Sorting arrays to non-decreasing (ascending or same) array using quick sort (using last index as the pivot)
    Using partition as the helper function

    Args : array of n numbers (n integers)
    Returns : Non-decreasing (ascending or same) array
    '''
    if l < r:

        # pi is the abbreviation of partition index.
        # The element in arr[pi] is currently in correct place
        pi = partition(arr, l, r)

        quick_sort(arr, l, pi-1)
        quick_sort(arr, pi+1, r)


    return(arr)


if __name__ == '__main__':
    unittest.main()