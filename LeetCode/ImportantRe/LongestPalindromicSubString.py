# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
# he main things to explain here:
# We are iterating through our string looking for palindromes, we fill in a dp table with what we find and use it for reference:

# a	b	a
# a	t	f	t
# b	0	t	f
# a	0	0	t
# We start our iterations from the bottom (reverse the range - range(n-1, -1, -1)), and build our solution up (bottom up).
# Our diagonal is always true as it means it's always 1 letter (you could think of the letters as idx's also (0,0), (1,1) etc.).
# Bottom row: is 'a' a pal? True.
# Middle row: is 'b' a pal? True, is 'ba' a pal? False.
# Top row: is 'a' a pal? True, is 'ab' a pal? False, is 'aba' a pal? True.

# The logic for recording the longest palindromes:

# ((j - i + 1) <= 3 if the length of the str is < 3
# eg. aba i= 0, j = 2, 2 - 0 + 1 = 3, here we dont care about the middle letter, and we know s[i] == s[j].
# eg. ab i= 0, j = 1, 1 - 0 + 1 = 2 this isn't valid? But we already know s[i] != s[j] so wouldn't have made it to this check.
# OR dp[i + 1][j - 1] - the last str before the current was a palindrome.
# We store the palindromes we find along with their length in ans and return the str associated with the max len.

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if(n < 2):
            return s
        dp, ans = [[0]*n for _ in range(n)], {}
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans[j-i+1] = s[i:j+1]
                else:
                    dp[i][j] = False
                # print(dp)
        # print(dp)
        # print(ans)
        return ans[max(ans)]