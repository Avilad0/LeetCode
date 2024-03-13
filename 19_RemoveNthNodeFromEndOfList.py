# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        iter = head
        prev = None

        for i in range(1,n):
            iter = iter.next
        
        if iter.next == None:
            return head.next
        
        iter = iter.next
        prev = head
        while iter.next!=None:
            iter = iter.next
            prev = prev.next

        prev.next = prev.next.next

        return head
