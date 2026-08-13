class Node{
    int val;
    Node next;
    public Node(int val){
        this.val = val;
        this.next = null;
    }
}

class MyLinkedList {

    private Node head;
    private int size;
    public MyLinkedList() {
        head = new Node(0);
        head.next = null;
    }
    
    public int get(int index) {
        if(index >= size) return -1;
        Node cur = head.next;
        for(int i = 0; i<index; i++){
            cur = cur.next;
        }
        return cur.val;
    }
    
    public void addAtHead(int val) {
        Node node = new Node(val);
        node.next = head.next;
        head.next = node;
        size+=1;
        
    }
    
    public void addAtTail(int val) {
        Node node = new Node(val);
        Node cur = head;
        for(int i=0; i<size; i++ ){
            cur = cur.next;
        }

        cur.next = node;
        size++;
    }
    
    public void addAtIndex(int index, int val) {
        if(index>size) return;

        Node node = new Node(val);
        Node cur = head;
        for(int i = 0; i<index; i++){
            cur = cur.next;
        }
        node.next = cur.next;
        cur.next = node;
        size++;
        
    }
    
    public void deleteAtIndex(int index) {
        if(index>=size) return;
        Node cur = head;
        for(int i = 0; i<index; i++){
            cur = cur.next;
        }
        cur.next = cur.next.next;
        size--;
  
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */