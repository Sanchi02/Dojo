# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        if(len(s)==1):
            return 1
        op = 0
        i,j = 0,0
        tracker = defaultdict(int)
        while(i<len(s) and j<=i):
            if(tracker[s[i]]==0):
                tracker[s[i]] += 1
                i += 1
            else:
                tracker[s[j]] -= 1
                tracker[s[i]] += 1
                j += 1
                while(tracker[s[i]]>1 and j<i):
                    tracker[s[j]] -= 1
                    j += 1
                i+=1
            op = max(op, i-j)
        return op