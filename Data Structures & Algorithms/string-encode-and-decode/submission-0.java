class Solution {

    public String encode(List<String> strs) {

        String encodedString = "";

        for(int i = 0; i< strs.size(); i++){
            for(char ch: strs.get(i).toCharArray()){
                encodedString+=ch;
            }
            encodedString+="§";
        }

        return encodedString;

    }

    public List<String> decode(String str) {

        List<String> list = new ArrayList<>();
        String buffer = "";
        for(char ch: str.toCharArray()){
            if(ch == '§'){
                list.add(buffer);
                buffer = "";
            }else{
                buffer+=ch;
            }
        }

        return list;

    }
}
