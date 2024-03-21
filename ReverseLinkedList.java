public class ReverseLinkedList{
    public static void main(String[] args){
        System.out.println(new Solution().reverseList(new ListNode(1, new ListNode(2,null))));
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        ListNode temp;
        while(curr!=null){
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr =temp;
        }

        return prev;
    }
}

