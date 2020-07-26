# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        ptr = 0
        for i in range(1,len(nums)):
            if(sum(nums[ptr:i+1])<nums[i]):
                ptr = i
            tmp = max(sum(nums[ptr:i+1]),nums[i])
            ans = max(ans,tmp)
            # print('sum(nums[ptr:i]) = {} nums[i] = {}, ans = {}, ptr={}'.format(sum(nums[ptr:i+1]),nums[i],ans,ptr))
            
        return ans