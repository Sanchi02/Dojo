# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(len(lists)==0):
            return None
        arr = []
        for l in lists:
            h = l
            if(h and h.next):
                while(h.next):
                    arr.append(h.val)
                    h = h.next
            if(h):
                arr.append(h.val)
        arr.sort()
        head = ListNode()
        node = head
        for val in arr:
            tmp = ListNode(val)
            node.next = tmp
            node = node.next
        return head.next
            
            