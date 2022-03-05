# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# We can recursively define the result of a merge operation on two lists as the following (avoiding the corner case logic surrounding empty lists):

# list1[0]+merge(list1[1:],list2)
# list2[0]+merge(list1,list2[1:])
# ​	
# list1[0]<list2[0]
# otherwise
# ​	

# Namely, the smaller of the two lists' heads plus the result of a merge on the rest of the elements.

# Algorithm

# We model the above recurrence directly, first accounting for edge cases. Specifically, if either of l1 or l2 is initially null, there is no merge to perform, so we simply return the non-null list. Otherwise, we determine which of l1 and l2 has a smaller head, and recursively set the next value for that head to the next merge result. Given that both lists are null-terminated, the recursion will eventually terminate.

# Approach 2: Iteration
# Intuition

# We can achieve the same idea via iteration by assuming that l1 is entirely less than l2 and processing the elements one-by-one, inserting elements of l2 in the necessary places in l1.

# Algorithm

# First, we set up a false "prehead" node that allows us to easily return the head of the merged list later. We also maintain a prev pointer, which points to the current node for which we are considering adjusting its next pointer. Then, we do the following until at least one of l1 and l2 points to null: if the value at l1 is less than or equal to the value at l2, then we connect l1 to the previous node and increment l1. Otherwise, we do the same, but for l2. Then, regardless of which list we connected, we increment prev to keep it one step behind one of our list heads.

# After the loop terminates, at most one of l1 and l2 is non-null. Therefore (because the input lists were in sorted order), if either list is non-null, it contains only elements greater than all of the previously-merged elements. This means that we can simply connect the non-null list to the merged list and return it.


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1==None):
            return l2
        elif(l2==None):
            return l1
        elif(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        
            