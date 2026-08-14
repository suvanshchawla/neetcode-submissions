// In the dynamic array solution I think going forward and backward time becomes O(1) since we can directly access the location if it exists, when we visit a new page, we need to keep in mind we have to keep track of the "length" of the array that we can access, by limiting it to the index of the last new visited page

class BrowserHistory {

    private int curr;
    private List<String> history;

    public BrowserHistory(String homepage) {
        history = new ArrayList<>();
        history.add(homepage);
        curr = 0;
    }
    
    public void visit(String url) {
        curr++;
        history = history.subList(0, curr);
        history.add(url);

    }
    
    public String back(int steps) {
        curr = Math.max(0, curr - steps);
        return history.get(curr);
    }
    
    public String forward(int steps) {
        curr = Math.min(history.size() - 1, curr + steps);
        return history.get(curr);
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */