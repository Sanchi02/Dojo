# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self,head):
        ctr = 0
        node = head
        while(node.next):
            ctr += 1
            node = node.next
        return (ctr+1,node)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(head == None):
            return head
        if(k==0):
            return head
        l,lastNode = self.getLength(head)
        if(k>l):
            # m = k%l
            k = k%l
        times = l-k
        if(times == 0):
            return head
        print(times)
        lastNode.next = head
        for i in range(times-1):
            head = head.next
        tmp = head.next
        head.next = None
        return tmp
            