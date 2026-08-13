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

        ListNode newListTemp = new ListNode(0);
        ListNode newList = newListTemp;

        while(list1 != null && list2 !=null){
            if(list1.val <= list2.val){
                newListTemp.next = list1;
                list1 = list1.next;
            }else{
                newListTemp.next = list2;
                list2 = list2.next;
            }

            newListTemp = newListTemp.next;
        }

        if(list1 !=null){
            newListTemp.next = list1;
        }

        if(list2 !=null){
            newListTemp.next = list2;
        }

        return newList.next;
    }
}