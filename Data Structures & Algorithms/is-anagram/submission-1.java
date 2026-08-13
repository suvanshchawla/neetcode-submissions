class Solution {
    public boolean isAnagram(String s, String t) {
        // Brute force way would be to just sort the strings and then compare them
        
        // We can solve this in a way in a couple of ways
        // 1. We can create 2 hashmaps and then compare each key value pair 
        // 2. We can create 2 arrays of size 26 
        // and then store the value at the index 65 - int(ascii(letter))
        // and then compare 2 arrays
        // let's try both

        if(s.length()!=t.length()){
            return false;
        }else{
            HashMap<Character, Integer> h1 = new HashMap<>();
            HashMap<Character, Integer> h2 = new HashMap<>();

            for(char ch: s.toCharArray()){
                h1.put(ch, h1.getOrDefault(ch, 0) + 1);
            }
            
            for(char ch: t.toCharArray()){
                h2.put(ch, h2.getOrDefault(ch, 0) + 1);

            }

            return h1.equals(h2);
        }
    }
        
}
