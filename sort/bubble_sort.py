#!/usr/bin/env python3
# coding: utf-8

import unittest

class Tests(unittest.TestCase):
    def array_testing(self, arr, rev_arg = False):
        expected = sorted(arr, reverse = rev_arg)
        result = bubble_sort(arr, reverse = rev_arg)
        self.assertEqual(result, expected)

    def test_small_1(self):
        self.array_testing([3, 5, 4, 2, 1])
        
    def test_small_2(self):
        self.array_testing([24, 53, 92, 11, 75])
        
    def test_repeat(self):
        self.array_testing([5, 3, 5, 4, 5, 2])
        
    def test_large(self):
        self.array_testing([4, 3, 2, 2, 1, 2 ,30, 2, 4, 5, 6, 25])

    def test_empty(self):
        self.array_testing([])
    
    def test_reverse(self):
        self.array_testing([4, 3, 2, 2, 1, 2 ,30, 2, 4, 5, 6, 25], rev_arg = True)


def bubble_sort(arr, reverse = False):

    ''' Sorting arrays to non-decreasing (ascending or same) array using Bubble Sort
    
    Args : array of n numbers (n integers)
    Returns : Non-decreasing (ascending or same) array
    '''

    # indexing from backwards
    for x in range(len(arr)-1, 0, -1):
        count = 0
        for i in range(x):
            if arr[i] > arr[i+1]:
                count += 1
                k = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = k
                
        if count ==0:
            if reverse == True:
                arr = arr[::-1]
            
            return(arr)

    
    if reverse:
        arr = arr[::-1]
    
    return(arr)


if __name__ == '__main__':
    unittest.main()

