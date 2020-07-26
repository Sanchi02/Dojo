# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

# Example 1:

# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"
# Example 2:

# Input:
# [
#   "z",
#   "x"
# ]

# Output: "zx"
# Example 3:

# Input:
# [
#   "z",
#   "x",
#   "z"
# ] 

# Output: "" 

# Explanation: The order is invalid, so return "".
# Note:

# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
        # print(in_degree)
        
        for first_word, second_word in zip(words,words[1:]):
            # print("first word ={}, second word = {}".format(first_word,second_word))
            for l1,l2 in zip(first_word, second_word):
                if(l1!=l2):
                    if l2 not in adj_list[l1]:
                        adj_list[l1].add(l2)
                        in_degree[l2] += 1
                    break
            else:
                if(len(second_word) < len(first_word)):
                        return ""
        # print(adj_list)
        # print(in_degree)
        
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        
        
        while(queue):
            # print(queue)
            # print(in_degree)
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if(in_degree[d] == 0):
                    queue.append(d)
                    
        if len(output) < len(in_degree):
            return ""
        return "".join(output)