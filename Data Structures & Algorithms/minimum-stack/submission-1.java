class MinStack {

    private ArrayList<Integer> list;
    public MinStack() {
        list = new ArrayList<>();
    }
    
    public void push(int val) {
        list.add(val);
    }
    
    public void pop() {
        list.remove(list.size() - 1);
    }
    
    public int top() {
        return list.get(list.size() - 1);
    }
    
    public int getMin() {

        int min = Integer.MAX_VALUE;
        for(int num: list){
            if(num < min){
                min = num;
            }
        }
        return min;
    }
}
