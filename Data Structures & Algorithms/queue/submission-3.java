class QueueNode {
    int val;
    QueueNode next;
    QueueNode prev;

    public QueueNode(int val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}
class Deque {

    int size;

    QueueNode head;
    QueueNode tail;

     public Deque() {
        head = null;
        tail = null;
        size = 0;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void append(int value) {
       QueueNode node = new QueueNode(value);
       if(isEmpty()){
        head = tail = node;
       }else{
            node.prev = tail;
            tail.next = node;
            tail = node;
       }
       
       size++;
    }

    public void appendleft(int value) {
        QueueNode node = new QueueNode(value);
        if(isEmpty()){
            head = tail = node;
        }else{
            node.next = head;
            head.prev = node;  
            head = node;
        }
        size++;
    }

    public int pop() {
        if (isEmpty()) return -1;
        int val = tail.val;
        if (size == 1) {
            head = tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        size--;
        return val;
    }

    public int popleft() {
        if (isEmpty()) return -1;
        int val = head.val;
        if (size == 1) {
            head = tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        size--;
        return val;
    }
}
