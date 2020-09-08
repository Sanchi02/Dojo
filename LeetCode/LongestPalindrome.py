# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        tracker = defaultdict(int)
        for ch in s:
            tracker[ch] += 1
        flag = False
        count = 0
        for val in tracker:
            if(tracker[val]%2==0):
                count += tracker[val]
            else:
                flag = True
                count = count + tracker[val] -1
        if(flag):
            return count+1
        return count
            
        