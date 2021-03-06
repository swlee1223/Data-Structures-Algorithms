#!/usr/bin/env python3
# coding: utf-8

from typing import Lists
import numpy as np
from itertools import combinations
import unittest

class Tests(unittest.TestCase):
    def best_share_testing(self, a, b):
        expected = set(best_share_sort(a,b))
        result = set(best_share_dp(a, b))
        self.assertEqual(result, expected)

    # # checking special cases
    def test_empty(self):
        self.best_share_testing([], [])

    # # checking randomly generated cases
    def test_pa3_1(self):
        self.best_share_testing([2,1], [1,2])

    def test_pa3_2(self):
        self.best_share_testing([10,20,30,40], [8,8,25,35])

    def test_pa3_3(self):
        self.best_share_testing([10,10,10,10], [7,9,11,13])

    def test_random_size6(self):
        a = [63653, 96451, 96808, 54126, 58883, 82207]
        b = [13473, 11908, 77288, 51599, 30869, 69003]
        self.best_share_testing(a, b)

    def test_random_size8(self):
        a = [51469, 37963, 17943, 33488,     3, 57854,  9780, 90366]
        b = [13686, 20714, 99923, 19556, 93388, 14281, 11766, 25300]
        self.best_share_testing(a, b)

    def test_random_size10(self):
        a = [33164, 34538, 31644, 36679, 19825, 16955, 33526, 69582, 27827, 33000]
        b = [82389,  1808, 80838, 86110, 51146, 92398, 72462,  7417, 38048, 56499]
        self.best_share_testing(a, b)

    # # testing when the happiness is same.
    def test_same_happy_small(self):
        self.best_share_testing([5,5], [5,5])

    def test_same_happy_big(self):
        self.best_share_testing([10,10,10,10,10,10,10,10,10,10], [10,10,10,10,10,10,10,10,10,10])

    # # testing when it can have multiple solutions.
    def test_multi_sol_2C1(self):
        self.best_share_testing([2,2], [1,1])

    def test_multi_sol_4C2(self):
        self.best_share_testing([2,2,2,2], [1,1,1,1])

    def test_multi_sol_6C3(self):
        self.best_share_testing([2,2,2,2,2,2], [3,3,3,3,3,3])

    # # test non-increasing or non-decreasing input
    def test_non_increasing(self):
        self.best_share_testing([6,5,4,3,2,1], [6,5,4,3,2,1])


    def test_non_decreasing(self):
        self.best_share_testing([1,2,3,4,5,6], [1,2,3,4,5,6])

    def test_mixed_di(self):
        self.best_share_testing([1,2,3,4,5,6],[6,5,4,3,2,1])

    def test_unbalanced(self):
        self.best_share_testing([10,10,1,1], [100, 100, 0, 0])

    # # check if it handles exception
    def test_odd_sort(self):
        with self.assertRaises(Exception) : best_share_sort([5,3,1], [4,1,2])

    def test_odd_dp(self):
        with self.assertRaises(Exception) : best_share_dp([5,3,1], [4,1,2])



def best_share_sort(a : List[int], b: List[int]) -> List[int]:

    '''
    Computes total happiness for all a and b pairs and returns the combination of items where the happiness reaches the maximum
    
    (input) a : a's happiness score for each i rod
    (input) b : b's happiness score for each i rod
    (output) : combinatin of items where the total happiness reached the maxiumum 
    '''

    
    if len(a) % 2 or len(b) % 2 ==1:
        raise Exception("Please check if the lists are even sized.")
    

    # calculate the difference and sort it based on its values.
    diff = []
    for i in range(len(a)):
        diff.append([i, a[i]-b[i]])

    diff.sort(key = lambda x: x[1])

    res = [diff[i][0] for i in range(len(diff)//2, len(diff))]
    
    return res
    

########################################
############ Time Complexity ###########
# Running Time Complexity : nlogn      #
# - creating diff matrix: O(n)         #
# - sorting diff matrix : O(nlogn)     #
# - getting all 0th index from sorted  #  
# : O(n/2)                             #
#                                      #
# Memory Complexity : n                #
# - array n for storing diff array     #
########################################
########################################


def best_share_dp(a, b):
    '''
    Computes total happiness for all a and b pairs and returns the combination set where the happiness reaches the maximum. This is implemented using dynamic programming.
    
    (input) a : a's happiness score for each i rod
    (input) b : b's happiness score for each i rod
    (output) : combinatin set where the total happiness reached the maxiumum 
    '''


    if len(a) % 2 or len(b)%2 ==1:
        raise Exception("Please check if the lists are even sized.")
    

    # This 2-d array will save the maximum happiness for given i and j.
    # i : number of items that has been distributed. Range [0, n+1)
    # j : number of items that Alice has earned. Range [0, n/2+1)

    # When i < j : Nonsensical. i is the number of total items distributed so it always has to be larger or equal to j.
    # Also when i + N/2 -j > N : Alice and Bob has to have equal number of items

    dp = np.array([[-1 for j in range(len(a)//2+1)] for i in range(len(a)+1)])
    dp[0,0] = 0

    ### BASE CASE
    # [i,j] interpretation: i items distributed and j items went to Alice

    # Giving till n to Bob: incrementing only i and keep j=0 
    for i in range(1, len(a)+1):
        dp[i, 0] = sum(b[0:i])

    # Giving till n/2 to Alice: incrementing i and j at same time. (# of Given items  = # of Given items to Alice)
    for i in range(1,len(a)//2+1):
        dp[i, i] = sum(a[0:i])
        
    for j in range(1, len(a)//2+1):
        for i in range(j+1, len(a)+1):
            # h_a: Happiness when you are giving your current element to Alice.
            # You look at the previous best step (j-1, i-1), and calculate happiness by adding a's happiness of index i
            h_a = dp[i-1, j-1] + a[i-1]

            # h_b: Happiness when you are giving your current element to Bob.
            # You look at the previous best step (i-1, j) (since you are not giving this element to Alice), and calculate happiness by adding b's happiness of index i

            h_b = dp[i-1, j] + b[i-1]


            dp[i, j] = max(h_a, h_b)

    def backtrack(dp):
        i, j= dp.shape[0]-1, dp.shape[1]-1
        alt = 1
        a_items = []
        b_items = []
        while i > 0 and j > 0:
            h_a = dp[i-1, j-1] + a[i-1]
            h_b = dp[i-1, j] + b[i-1]
            if dp[i,j] == h_a:
                a_items.append(i-1)
                j-=1

            i-=1

        return(a_items)


    return(backtrack(dp))


#########################################
############ Time Complexity ############
# Total Running Time Complexity : n^2   #
# - creating base case of Bob : O(n)    #
# - creating base case of Alice : O(n/2)#
# - recursion: O(n^2)                   #
# - backtrack : O(n)                    #  
#                                       #
# Memory Complexity :                   # 
# n *n/2 = n^2/2 =O(n^2)                #
#########################################
#########################################


if __name__ == '__main__':
  unittest.main()