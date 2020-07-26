# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        next_level = [root]
        current_level = []
        
        while(root and next_level):
            current_level = copy.deepcopy(next_level)
            next_level = []
            tmp = []
            
            for node in current_level: 
                tmp.append(node.val)
                if(node.left):
                    next_level.append(node.left)
                if(node.right):
                    next_level.append(node.right)
            queue.append(copy.deepcopy(tmp))
        return queue[::-1]