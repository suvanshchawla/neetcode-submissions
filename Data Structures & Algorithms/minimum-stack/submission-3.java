class MinStack {

    private ArrayList<Integer> list;
    private ArrayList<Integer> minList;
    

    public MinStack() {
        list = new ArrayList<>();
        minList = new ArrayList<>();
    }
    
    public void push(int val) {
        if (minList.isEmpty()) {
            minList.add(val);
        } else {
            int prevMin = minList.get(minList.size() - 1);
            minList.add(Math.min(val, prevMin));
        }
        list.add(val);
    }
    
    public void pop() {
        list.remove(list.size() - 1);
        minList.remove(minList.size() - 1);
    }
    
    public int top() {
        return list.get(list.size() - 1);
    }
    
    public int getMin() {
        return minList.get(minList.size() - 1);
    }
}
