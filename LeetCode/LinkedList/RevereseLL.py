# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev = None
#         nextPtr = head
#         while(nextPtr):
#             tmp = nextPtr.next
#             nextPtr.next = prev
#             prev = nextPtr
#             nextPtr = tmp
        
#         return prev

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head == None or head.next==None):
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        