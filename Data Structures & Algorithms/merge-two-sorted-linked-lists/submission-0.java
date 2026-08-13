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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        
        ListNode nl = new ListNode();
        ListNode head = new ListNode();
        head.next = nl;
        ListNode curr1, curr2;

        curr1 = list1;
        curr2 = list2;

        while(curr1 != null && curr2 != null){
            if(curr1.val <= curr2.val){
                nl.next = curr1;
                nl = curr1;
                curr1 = curr1.next;
            }else{
                nl.next = curr2;
                nl = curr2;
                curr2 = curr2.next;
            }
        }

        if(curr1!=null){
            nl.next = curr1;
        }
        if(curr2!=null){
            nl.next = curr2;
        }

        return head.next.next;
        // System.out.println(list1);
        // System.out.println(list2);
        // System.out.println(curr1);
        // System.out.println(curr2);
        // return new ListNode();
        
    }
}