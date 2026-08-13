class Url{
    String url;
    Url next;
    Url prev;

    public Url(String url){
        this.url = url;
        this.next = null;
        this.prev = null;
    }
}

// We can create a Url class, that will hold the string url, and link the last visited webpage and the next which could be filled when we visit a new url


class BrowserHistory {

    private Url curr;

    public BrowserHistory(String homepage) {
        curr = new Url(homepage);
        
        // We need a linked list that keeps track of the urls
        // we also need a curr page pointer to mark where we are right now
        
    }
    
    public void visit(String url) {
        //When given a url we can simply create a new node, 
        Url page = new Url(url);
        page.prev = curr;
        curr.next = page;
        curr = curr.next;
        
    }
    
    public String back(int steps) {
        // to go back
        int i = 0;
        while(i < steps && curr.prev != null){
            curr = curr.prev;
            i++;
        }

        return curr.url;
        // while i < steps && curr.prev is not null
        // curr = curr.prev
        //return curr.url
    }
    
    public String forward(int steps) {
        //to go forward
        // while i < steps && curr.next is not null
        //curr = curr.next
        // return curr.url

        int i = 0;
        while(i < steps && curr.next!= null){
            curr = curr.next;
            i++;
        }

        return curr.url;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */