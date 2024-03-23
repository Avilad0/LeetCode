# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

#Solution 2 without extra array
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head == None or head.next == None or head.next.next == None:
            return

        s,f = head,head
        while f.next!=None and f.next.next!=None:
            s = s.next
            f = f.next.next

        m = s
        s=s.next
        m.next = None
        prev = None
        while s!=None:
            t = s.next
            s.next = prev
            prev = s
            s = t
        
        f = head
        while prev:
            t = f.next
            f.next = prev
            prev = prev.next
            f.next.next = t
            f=t
        



# Solution 1 with extra array space
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:

#         if head == None or head.next == None or head.next.next == None:
#             return

#         t = head
#         ref = []
    
#         while t!=None:
#             ref.append(t)
#             t=t.next
        
#         head = ref[0]
#         l = len(ref)

#         b = ListNode(-1,None)
#         for i in range(l//2):
#             f = ref.pop(0)
#             b.next = f 

#             b = ref.pop()
#             f.next = b

#         if len(ref)!=0:
#             b.next = ref.pop()
#             b.next.next = None
#         else:
#             b.next = None

#         print(ref)


l =ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
    
l = Solution().reorderList(l)