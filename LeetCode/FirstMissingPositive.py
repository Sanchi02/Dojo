# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Follow up:

# Your algorithm should run in O(n) time and uses constant extra space.
# https://www.youtube.com/watch?v=-lfHWWMmXXM&t=660s
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            correctPos = nums[i] - 1
            while(nums[i] <= n and nums[i] >= 0 and nums[i]!=nums[correctPos]):
                nums[i],nums[correctPos] = nums[correctPos], nums[i]
                correctPos = nums[i] - 1
        
        # print(nums)
        for ind,val in enumerate(nums):
            if(ind+1!=val):
                return ind+1
        
        return n-1