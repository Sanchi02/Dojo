# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i,j):
            for t in range(i,j):
                if(s[t] != s[j-t+i]):
                    return False
            return True
        size = len(s)
        for i in range(size//2):
            j = size-i-1
            if(s[i]!=s[j]):
                return (isPalindrome(i+1,j) or isPalindrome(i,j-1))
        return True