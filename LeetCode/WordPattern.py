# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:

# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:

# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:

# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, stringy: str) -> bool:
        tracker = defaultdict(str)
        tracker2 = defaultdict(str)
        listOfWords = [w for w in stringy.split(' ')]
        if(len(pattern)!=len(listOfWords)):
            return False
        for i,c in enumerate(pattern):
            if(listOfWords[i] in tracker or c in tracker2):
                if(tracker[listOfWords[i]] != c or tracker2[c] != listOfWords[i]):
                    return False
            else:
                tracker[listOfWords[i]] = c
                tracker2[c] = listOfWords[i]
        print(tracker)
        print(tracker2)
        return True
        