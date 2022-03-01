# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        head = tmp
        carry = 0
        ptr1 = l1
        ptr2 = l2
        while(ptr1 or ptr2):
            if(ptr1):
                x=ptr1.val
                ptr1 = ptr1.next
            else:
                x=0
            if(ptr2):
                y=ptr2.val
                ptr2 = ptr2.next
            else:
                y=0
            sumR = x+y+carry
            
            tmp.next = ListNode(sumR%10)
            carry = sumR//10
            tmp = tmp.next
        if(carry > 0):
            tmp.next = ListNode(carry)
        return head.next