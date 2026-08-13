class Solution {
    public boolean isValid(String s) {
       
       Stack<Character> stack = new Stack<>();
       Map<Character, Character> closeToStart = new HashMap<>(Map.of(
        ')', '(',
        '}', '{',
        ']', '['
       ));

       for(char c: s.toCharArray()){
        if(!stack.isEmpty() && closeToStart.containsKey(c)){
            if(stack.peek() == closeToStart.get(c)){
                stack.pop();
            }else{
                return false;
            }
        }else{
            stack.push(c);
        }
       

       }

        return stack.isEmpty();

    }
}

