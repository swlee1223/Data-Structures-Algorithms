#!/usr/bin/env python3
# coding: utf-8

import unittest
import numpy as np
import random



class Tests(unittest.TestCase):
    def array_testing(self, arr):
        expected = list(sorted(arr))
        result = list(quick_sort_dual(arr))
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


def quick_sort_dual(arr):
    ''' Sorting arrays to non-decreasing (ascending or same) array using Dual-Pivot Randomized Quick Sort
    

    Q. What is a Dual-Pivot Randomized Quicksort?
    - Selecting 2 random pivots which divide the array into 3 parts.

    It chooses 2 pivots which are first and second and each of the pivots puts elements that is smaller to the left and bigger to the right.
    
    Args : array of n numbers (n integers)
    Returns : Non-decreasing (ascending or same) array
    '''


    arr = list(arr)


    def compare(x, y):
        ''' This function compares the first and second elements and returns the sorted list'''
        if x > y:
            x, y = y, x

        return([x,y])


    if len(arr) <= 1:
        return arr

    
    elif len(arr) == 2:
        compare(arr[0], arr[1])

    k1, k2 = compare(arr.pop(0), arr.pop(0))

    # a is for part where <k1, b is k1 < arr[j] < k2, c is > k2
    A, B, C = [], [], []
    for j in arr:
        # When current element is bigger than k2 ==> append it to C
        if  k2 <= j:
            C.append(j)

        # When current element is between k1 and k2
        elif k1 <= j < k2:
            # Swapping only happens when current element is smaller than either one of the pivot.
            # So if the current element is smaller than the pivot, you swap the current pointed array, which is equal or greater with the pivot.
            B.append(j)
        
        # finding position for k1
        # it increments s1 by 1 when the pivot is larger than current j
        elif k1 > j :
            A.append(j)

    return(quick_sort_dual(A) + [k1] + quick_sort_dual(B) + [k2] + quick_sort_dual(C))


if __name__ == '__main__':
    unittest.main()