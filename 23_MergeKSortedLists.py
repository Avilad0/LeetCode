from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Using Merge sort : tc: O(nlogk), sc: O(logk)
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return None
        
        return self.mergeSort(lists, 0, len(lists)-1)
    
    def mergeSort(self, lists, left, right):
        if left>right:
            return None
        
        if left==right:
            return lists[left]
        
        mid = (left+right)//2
        list1 = self.mergeSort(lists, left, mid)
        list2 = self.mergeSort(lists, mid+1, right)

        return self.mergeTwoSortedLists(list1, list2)
    
    def mergeTwoSortedLists(self, list1, list2):
        
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val<list2.val:
                curr.next = list1
                list1=list1.next
            else:
                curr.next = list2
                list2= list2.next
            curr=curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next
    


# # Using heap tc: O(nlogk), sc: O(k)
# import heapq
# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if lists == None:
#             return None
        
#         if len(lists)==1:
#             return lists[0]
        
#         heap = []
#         for i in range(len(lists)):
#             if lists[i]:
#                 # need i to prevent ListNode undefined comparison 
#                 # We can also create a wrapper of ListNode class to support __lt__ operation
#                 heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
#         dummyHead = ListNode()
#         curr = dummyHead
#         while heap:
#             (val, i, node) = heapq.heappop(heap)

#             curr.next = node
#             curr = curr.next

#             node = node.next
#             if node:
#                 heapq.heappush(heap, (node.val, i, node))
        
#         return dummyHead.next