# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        if(len(strs)==1):
            return strs[0]
        common = strs[0]
        for i in range(1,len(strs)):
            ptr = 0
            for letter, cletter in zip(strs[i],common):
                if(letter == cletter):
                    ptr += 1
                else:
                    break
            common = strs[i][:ptr]
        return common
                    
            
            
                