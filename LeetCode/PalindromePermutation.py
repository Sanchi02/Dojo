# Given a string, determine if a permutation of the string could form a palindrome.

# Example 1:

# Input: "code"
# Output: false
# Example 2:

# Input: "aab"
# Output: true
# Example 3:

# Input: "carerac"
# Output: true

from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if(len(s)%2==0):
            evenFlag = True
        else:
            evenFlag = False
        tracker = defaultdict(int)
        for c in s:
            tracker[c] += 1
        countOfOdd = 0
        for item in tracker:
            if(tracker[item]%2==1):
                countOfOdd += 1
        if(evenFlag and countOfOdd >0):
            return False
        elif(evenFlag == False and countOfOdd>1):
            return False
        return True