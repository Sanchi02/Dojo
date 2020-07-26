# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while (left <= right):
            mid = ((left+right)//2)
            if ((mid*(mid+1))//2 == n):
                return mid
            if((mid*(mid+1))//2 > n):
                right = mid - 1
            else:
                left = mid + 1
        return right
            
        