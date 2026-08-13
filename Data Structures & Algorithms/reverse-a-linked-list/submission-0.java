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
           //Reversing a linked list can be done iteratively
           // create 3 nodes - prev, curr and temp
           // and reverse the list one node at a time, 
           // store the value of current forward in temp
           ListNode curr = head;
           ListNode prev = null;
           

           while(curr!=null){
           ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            
           }

           return prev;
           

    }
}
