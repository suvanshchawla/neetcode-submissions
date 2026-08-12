/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
       
       // there are two ways to do it, let's first try to write the iterative method where we can use 2 pointers, one is prev and the other is current, where we go on one by one reversing the linked list

       ListNode prev = null;
       ListNode curr = head;

       while(curr!=null){
        ListNode temp = curr.next;
        
        curr.next = prev;
        prev = curr;
        curr = temp;

       }

       return prev;

    }
}