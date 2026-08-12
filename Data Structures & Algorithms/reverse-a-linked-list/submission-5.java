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

       // now let's try the other approach where we can use recursion, here we try to break the problem down into smaller problems. We have a base case, where if head.next is null then it is already reversed, so to say

        if(head == null){
            return null;
        }

        ListNode newHead = head;
        if (head.next!=null){
            newHead = reverseList(head.next);
            head.next.next = head;
        }

        head.next = null;
        return newHead;

    }

    
}