# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.


# class Solution:
#     def getMax(self, n, d):
#         while(n%d==0):
#             n = n//d
#         return n
            
#     def nthUglyNumber(self, n: int) -> int:
#         uglies = [1]
#         counter = 2
#         while(len(uglies) != n):
#             curr = counter
#             curr = self.getMax(curr,2)
#             curr = self.getMax(curr,3)
#             curr = self.getMax(curr,5)
#             if(curr == 1):
#                 uglies.append(counter)
            
#             counter += 1
#         print(uglies)
#         return(uglies[n-1])
    
from heapq import heappop, heappush

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = []
        ctr = 0
        flag = False
        heappush(uglies,1)
        while(ctr!=n):
            ctr += 1
            t = heappop(uglies)
            for n1 in [2,3,5]:
                if n1*t not in uglies:
                    heappush(uglies,t*n1)
        return t
        
        