# https://leetcode.com/problems/climbing-stairs/
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 0
        tracker = [0,1,2]
        for i in range(3,n+1):
            tmp = tracker[i-1] + tracker[i-2]
            tracker.append(tmp)
        return(tracker[n])
            
#         def backtrack(curr):
#             if(curr == n):
#                 total.append(1)
#             if(curr>n):
#                 return
#             backtrack(curr+1)
#             backtrack(curr+2)
            
#         backtrack(0)
#         return len(total)
