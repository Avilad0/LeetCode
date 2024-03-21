from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        prev = None
        curr = head
        while curr!=None:
            nxt = curr.next
            curr.next=prev
            prev = curr
            curr = nxt
        return prev


l =ListNode(1,ListNode(2,None))
    
l = Solution().reverseList(l)


while l!=None:
    print(l.val)
    l = l.next
