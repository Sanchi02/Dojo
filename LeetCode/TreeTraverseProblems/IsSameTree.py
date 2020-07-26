# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         tree1 = self.BfsTraversal(p)
#         tree2 = self.BfsTraversal(q)
#         # print(tree1)
#         # print(tree2)
#         return (tree1==tree2)
        
#     def BfsTraversal(self,root):
#         currLevel = []
#         nextLevel = [root]
#         nodes = []
#         while(nextLevel):
#             currLevel = nextLevel
#             nextLevel = []
#             for n in currLevel:
#                 if(n!=None):
#                     nodes.append(n.val)
#                     if(n.left):
#                         nextLevel.append(n.left)
#                     else:
#                         nextLevel.append(None)
#                     if(n.right):
#                         nextLevel.append(n.right)
#                     else:
#                         nextLevel.append(None)
#                 else:
#                     nodes.append(None)
#         return nodes
                
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if(p.val!=q.val):
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
                
                