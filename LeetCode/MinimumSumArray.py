# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        length = 99999
        left = 0
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            while(tot >= s):
                length = min(length, i+1-left)
                tot -= nums[left]
                left += 1
        if(length == 99999):
            return 0
        else:
            return length