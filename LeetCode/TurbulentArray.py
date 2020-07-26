# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.

 

# Example 1:

# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:

# Input: [4,8,12,16]
# Output: 2
# Example 3:

# Input: [100]
# Output: 1
 

# Note:

# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        B = []
        if(len(A)==1):
            return 1
        for i in range(1,len(A)):
            if(A[i-1]>A[i]):
                B.append(1)
            elif(A[i-1]<A[i]):
                B.append(-1)
            else:
                B.append(0)
        print(B)
        maxLen = 0
        anchor = 0
        i = 0
        while(i<len(B)-1):
            maxLen = max(maxLen, i-anchor+1)
            # print("maxLen = {}, anchor ={}, i ={}".format(maxLen,anchor,i))
            if(B[i]*B[i+1]!=-1):
                anchor = i+1
            i += 1 
            
        if(B[i]*B[i-1]==-1):
            maxLen = max(maxLen, i-anchor+1)
        if(B.count(1)==len(B) or B.count(-1)==len(B)):
            return 2
        elif(B.count(0)==len(B)):
            return 1
        return maxLen+1
            
                