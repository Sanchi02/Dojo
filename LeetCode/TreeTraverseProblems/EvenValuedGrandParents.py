# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.

 

# Example 1:



# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        curr_level = []
        next_level = [root]
        arrF = []
        while(root and next_level):
            curr_level = next_level
            next_level = []
            for node in curr_level:
                if(node.val%2==0):
                    if(node.left):
                        if(node.left.left):
                            arrF.append(node.left.left.val)
                        if(node.left.right):
                            arrF.append(node.left.right.val)
                    if(node.right):
                        if(node.right.left):
                            arrF.append(node.right.left.val)
                        if(node.right.right):
                            arrF.append(node.right.right.val)
                if(node.left):
                    next_level.append(node.left)
                if(node.right):
                    next_level.append(node.right)
        return sum(arrF)