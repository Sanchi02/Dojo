# Given an input string, reverse the string word by word.

 

# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Follow up:

# For C programmers, try to solve it in-place in O(1) extra space.
class Solution:
    def reverseWords(self, s: str) -> str:
        # words = []
        # anchor = 0
        # spaceFlag = True
        # for i in range(len(s)):
        #     if(s[i]==' ' and spaceFlag==False):
        #         # print("Appending!!!Anchor = {}, spaceFlag = {}, i= {}".format(anchor,spaceFlag, i))
        #         words.append(s[anchor:i])
        #         spaceFlag = True
        #         anchor = i+1
        #     if(s[i] != ' '):
        #         spaceFlag = False
        #     if(spaceFlag==True):
        #         anchor = i+1
        #     # print("Anchor = {}, spaceFlag = {}, i= {}".format(anchor,spaceFlag, i))
        #         # anchor = i+1
        # if(spaceFlag==False):
        #     words.append(s[anchor:])
        # # print(words)
        # words = words[::-1]
        # rstr = ''
        # for i,w in enumerate(words):
        #     rstr += w
        #     if(i!=len(words)-1):
        #         rstr += ' '
        # return rstr
        return " ".join(reversed(s.split()))
            
                
            
            
        