# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
from copy import deepcopy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = []
        for i,s in enumerate(strs):
            tmp = list(s)
            tmp.sort()
            tracker.append((tmp,i))
        tracker.sort()
        # print(tracker)
        op = []
        ptr = 1
        prev = tracker[0][0]
        tmp = [strs[tracker[0][1]]]
        while(ptr<len(tracker)):
            if(tracker[ptr][0]==prev):
                tmp.append(strs[tracker[ptr][1]])
            else:
                op.append(deepcopy(tmp))
                prev = tracker[ptr][0]
                tmp = [strs[tracker[ptr][1]]]
            ptr += 1
        op.append(deepcopy(tmp))
        return op
    
# class Solution(object):
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()
                