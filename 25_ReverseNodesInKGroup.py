# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# # tc=O(n), sc=O(1), same as below with optimised curr.next assignment after reversing
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #reverse k nodes
        def reverse(start):
            prev1, curr1 = None, start 
            for _ in range(k):
                tmp = curr1.next
                curr1.next=prev1
                prev1 = curr1
                curr1=tmp

            return prev1

        dummy = ListNode(0,head)
        prev = dummy    #prev points to last node of prev group
        curr = head

        while curr:
            nxt = curr  #nxt point to head of next group
            #check if next k nodes present or return
            for _ in range(k):
                if not nxt:
                    return dummy.next

                nxt = nxt.next
            
            currNew = reverse(curr)

            prev.next = currNew    #add reversed next to prev
            curr.next = nxt #add start of next group to end of reversed
            prev=curr   # update prev to curr - last node of group
            curr=curr.next  # increment curr
        
        return dummy.next


# # tc=O(n), sc=O(1), same as above 
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         #reverse k nodes
#         def reverse(start):
#             prev1, curr1 = None, start 
#             for _ in range(k):
#                 tmp = curr1.next
#                 curr1.next=prev1
#                 prev1 = curr1
#                 curr1=tmp

#             return prev1

#         dummy = ListNode(0,head)
#         prev = dummy    #prev points to last node of prev group
#         curr = head

#         while curr:
#             nxt = curr  #nxt point to head of next group
#             #check if next k nodes present or return
#             for _ in range(k):
#                 if not nxt:
#                     return dummy.next

#                 nxt = nxt.next
            
#             curr = reverse(curr)

#             prev.next = curr    #add reversed next to prev
#             for _ in range(k-1):
#                 curr=curr.next
#             curr.next = nxt #add start of next group to end of reversed
#             prev=curr   # update prev to curr - last node of group
#             curr=curr.next  # increment curr
        
#         return dummy.next
            