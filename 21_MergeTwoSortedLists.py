from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution with dummy node, tc:O(m+n), sc:O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newHead = ListNode()
        curr = newHead

        while list1 and list2:
            if list1.val<=list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        
        if list1:
            curr.next=list1
        if list2:
            curr.next=list2

        return newHead.next


# # Iterative solution without dummy node, tc:O(m+n), sc:O(1)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1==None:
#             return list2
#         if list2==None:
#             return list1

#         p1, p2 = list1, list2

#         newHead = list1
#         if list2.val< list1.val:
#             newHead = list2
#             p2 = list2.next
#         else:
#             p1 = list1.next
        
#         curr = newHead
#         while p1 and p2:
#             if p1.val<=p2.val:
#                 curr.next=p1
#                 p1=p1.next
#             else:
#                 curr.next=p2
#                 p2=p2.next
#             curr=curr.next
        
#         if p1:
#             curr.next=p1
#         if p2:
#             curr.next=p2

#         return newHead


# # Recursive solution tc:O(m+n), sc:O(m+n)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         if list1==None:
#             return list2
#         if list2==None:
#             return list1
        
#         if list1.val<=list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2