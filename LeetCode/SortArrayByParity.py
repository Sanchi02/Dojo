# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

 

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = len(A)-1
        while(ptr2>ptr1):
            if(A[ptr1]%2!=0):
                if(A[ptr2]%2==0):
                    A[ptr1],A[ptr2] = A[ptr2],A[ptr1]
                    ptr1 += 1
                    ptr2 -= 1
                else:
                    ptr2 -= 1
            else:
                ptr1 += 1
        return A
    
# class Solution(object):
#     def sortArrayByParity(self, A):
#         A.sort(key = lambda x: x % 2)
#         return A