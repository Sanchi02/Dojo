# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# https://www.youtube.com/watch?v=qC5DGX0CPFA
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        cs = []
        index = [-1]
        op = 0
        for ind,c in enumerate(s):
            # print("cs = {}, index= {}".format(cs,index))
            if(c=='('):
                cs.append(c)
                index.append(ind)
            elif(c==')' and cs and cs[-1]=='('):
                cs.pop()
                index.pop()
            else:
                index.append(ind)
            op = max(op, ind-index[-1])
        return op