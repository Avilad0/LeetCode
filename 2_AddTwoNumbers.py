from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# tc=O(max(m,n)), sc=O(1) (max(m,n)+1 space used in worst case for output and not computation)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        curr = newHead
        carry =0
        while l1 or l2 or carry:
            summ = carry
            if l1:
                summ+=l1.val
                l1=l1.next
            if l2:
                summ+=l2.val
                l2=l2.next
            digit, carry = summ%10, summ//10
            curr.next = ListNode(digit)
            curr=curr.next
        
        return newHead.next
            
