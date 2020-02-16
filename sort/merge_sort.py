#!/usr/bin/env python3
# coding: utf-8

import unittest
import numpy as np


class Tests(unittest.TestCase):
    def array_testing(self, arr):
        expected = list(sorted(arr))
        result = list(merge_sort(arr))
        self.assertEqual(result, expected)

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

def merge_sort(arr):
    ''' Sorting arrays to non-decreasing (ascending or same) array using merge Sort
    
    Args : array of n numbers (n integers)
    Returns : Non-decreasing (ascending or same) array
    '''
    
    ## base case
    if len(arr) <2:
        return(arr)

    else:        
        ## this is dividing part
        left = arr.copy()[:len(arr)//2]
        right = arr.copy()[len(arr)//2:]
 
        ## this is recursion part:  trust that it sorts everything at the end
        merge_sort(left)
        merge_sort(right)

        ## merge part : l_i, r_i and a_i is the abbreviation of Left Index, Right Index, Array Index
        l_i = r_i = a_i = 0
        
        ## while loop : checking from the first index of left and right chunks to the last index of either left or right chunk
        while l_i < len(left) and r_i < len(right):
            # when right is bigger than the left
            if left[l_i] < right[r_i]:
                arr[a_i] = left[l_i]
                l_i += 1
                
            else:
                arr[a_i] = right[r_i]
                r_i += 1
            
            a_i += 1
        
        ## while loop: this is for leftovers. If right(left) has gone to the end of its index but left(right) didn't, this part will take charge to put them in leftovers.
        while l_i < len(left):
            arr[a_i] = left[l_i]
            l_i += 1
            a_i += 1

        while r_i < len(right):
            arr[a_i] = right[r_i]
            r_i += 1
            a_i += 1
            
        return(arr)    

if __name__ == '__main__':
    unittest.main()