# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if(head==None):
            return head
        while(head.val == val):
            head = head.next
            if(head==None):
                return head
        currNode = head
        while(currNode and currNode.next):
            prevNode = currNode
            currNode = currNode.next
            while(currNode and currNode.val == val):
                prevNode.next = currNode.next
                currNode.next = None
                currNode = prevNode.next
            
        return head