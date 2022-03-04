# https://leetcode.com/problems/counting-bits/ 
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
 

# Constraints:

# 0 <= n <= 105
 

# Follow up:

# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
class Solution:
    def countBits(self, n: int) -> List[int]:
        if(n==0):
            return [0]
        if(n==1):
            return [0,1]
        tracker = [-1 for i in range(n+1)]
        tracker[0] = 0
        tracker[1] = 1
        tracker[2] = 1
        
        
        def recursive(n,tracker):
            # print(n)
            if(n%2==0 and tracker[n]==-1):
                tracker[n] = recursive(n//2,tracker)
                return tracker[n]
            elif(n%2==1 and tracker[n]==-1):
                tracker[n]=1+recursive(n//2,tracker)
                return tracker[n]
            elif(n%2==1):
                tracker[n] = 1+tracker[n//2]
                return tracker[n]
            else:
                tracker[n]=tracker[n//2]
                return tracker[n]
        
        for i in range(3,n+1):
            recursive(i,tracker)
            
        return tracker