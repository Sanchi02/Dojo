# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# Note: Answer will in the range of 32-bit signed integer.

import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        return self.rec(root)
        
    def rec(self,root):
        next_level = [(root,0,0)]
        curr_level = []
        max_level = []
        level_ctr = 0
        while(next_level and root):
            curr_level = next_level
            next_level = []
            level_ctr += 1
            for node in curr_level:
                if(node[0].left):
                    next_level.append((node[0].left,level_ctr,2*node[2]))
                if(node[0].right):
                    next_level.append((node[0].right,level_ctr,(2*node[2])+1))
            tmp = curr_level[len(curr_level)-1][2] - curr_level[0][2]
            max_level.append(tmp)
        return max(max_level)+1  