# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        val = "{:0b}".format(num)
        val = list(val)
        if(len(val)<=2):
            if(len(val)==1 and val[0]=='1'):
                return True
            return False
        return max(val[1:])=='0' and len(val[1:])%2==0