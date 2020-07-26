# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = 2**len(nums)
        powerSet = []
        for i in range(size):
            tmp = []
            binary = '{0:b}'.format(i)
            if(len(binary)<len(nums)):
                t = len(nums)-len(binary)
                t = '0'*t
                binary = t + binary
            # print(binary)
            for j,b in enumerate(binary):
                if(b=='1'):
                    tmp.append(nums[j])
            powerSet.append(copy.deepcopy(tmp))
        return powerSet