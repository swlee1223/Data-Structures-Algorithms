#!/usr/bin/env python3
# coding: utf-8

import unittest
class Tests(unittest.TestCase):
    def array_testing(self, arr):
        expected = sorted(arr)
        result = insertion_sort(arr)
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
    

def insertion_sort(arr):
    # this is the index for j (the key)
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1

        # this is the index for i (scan in reverse order)
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1

        arr[i+1] = key
    return(arr)



if __name__ == '__main__':
    unittest.main()
