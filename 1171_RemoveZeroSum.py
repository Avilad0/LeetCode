# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dp = []
        # i=0
        # while head!=None:
        #     temp = head
        #     dp_t =[0]*i
        #     while temp!=None:
        #         temp = temp.next
        #         dp_t.append
        #     head = head.next
        #     i+=1

        check = head
        prev = None
        while check!=None:
            sum = 0
            curr = check
            while curr!=None:
                sum +=curr.val
                if sum == 0:
                    if prev == None:
                        head = curr.next
                        check = curr.next
                    else:
                        prev.next = curr.next
            
                curr = curr.next

            if check == None:
                break
            prev = check
            check = check.next

        return head