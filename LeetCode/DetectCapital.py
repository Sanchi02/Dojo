# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
 

# Example 1:

# Input: "USA"
# Output: True
 

# Example 2:

# Input: "FlaG"
# Output: False
 

# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        tracker = []
        for w in word:
            if(w.isupper()):
                tracker.append(1)
            else:
                tracker.append(0)
        if(len(tracker)==1):
            return True
        print(tracker)
        if(tracker[0]==0):
            for i in range(1,len(tracker)):
                if(tracker[i]!=tracker[0]):
                    return False 
            return True
        else:
            if(tracker[0]== tracker[1]):
                for i in range(2,len(tracker)):
                    if(tracker[i]!=tracker[0]):
                        return False
                return True
            else:
                for i in range(1,len(tracker)):
                    if(tracker[i]==1):
                        return False
                return True
              
            
        