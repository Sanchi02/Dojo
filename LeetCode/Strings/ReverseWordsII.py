# Given an input string , reverse the string word by word. 

# Example:

# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note: 

# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?

class Solution:
    def reverseBoundary(self,s,start,end):
        while(start<end):
            s[end],s[start] = s[start],s[end]
            end -= 1
            start += 1
    
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]
        
        anchor = 0
        print(s)
        for i, l in enumerate(s):
            if(l==' '):
                lenB = i-anchor
                # print("Anchor = {}, i={}, lenB= {}".format(anchor,i,lenB))
                self.reverseBoundary(s,anchor,i-1)
                # print(s)
                anchor = i+1
        if(len(s)>0):
            self.reverseBoundary(s,anchor,i)
        # print(s)