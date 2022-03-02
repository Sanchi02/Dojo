# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,postfix = 1,1
        output = [1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            output[i] = prefix*nums[i-1]
            prefix *= nums[i-1]
        postfix = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            output[i] = postfix * output[i]
            postfix *= nums[i]
        return output
#         prefix = [1 for i in range(len(nums))]
#         postfix = [1 for i in range(len(nums))]
#         output = [1 for i in range(len(nums))]
        
#         prefix[0] = nums[0]
#         for i in range(1,len(nums)):
#             prefix[i] = prefix[i-1]*nums[i]
            
#         postfix[len(nums)-1] = nums[len(nums)-1]
#         for j in range(len(nums)-2,-1,-1):
#             postfix[j] = postfix[j+1]*nums[j]
            
#         output[0] = postfix[1]
#         output[len(nums)-1] = prefix[len(nums)-2]
#         for i in range(1,len(nums)-1):
#             output[i] = prefix[i-1]*postfix[i+1]
            
#         return output
        