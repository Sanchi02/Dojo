# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

# from collections import defaultdict
# import heapq
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         tracker = defaultdict(int)
#         tracker2 = defaultdict(list)
#         for n in words:
#             tracker[n] += 1
#         # print(tracker)    
#         tbd = [(value, key) for key,value in tracker.items()]
#         tbd.sort(reverse=True)
#         print(tbd)
        
#         for value,key in tbd:
#             tracker2[value].append(key)
#         tbd.sort()
#         finalList = []
#         for key in tracker2:
#             tracker2[key].sort()
#             for val in tracker2[key]:
#                 finalList.append(val)
       
#         print(finalList)
#         return finalList[:k]

class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]