class Solution {
    public int calPoints(String[] operations) {
        
        List<Integer> list = new ArrayList<>();
        for(String op: operations){

            if(op.equals("+")){

                int last = list.get(list.size() - 1);
                int secondlast = list.get(list.size() - 2);
                list.add(last + secondlast);

            } else if(op.equals("C")){
                
                list.remove(list.size() - 1);

            } else if(op.equals("D")){
                
                list.add(list.get(list.size() - 1)*2);

            } else{
                int value = Integer.parseInt(op);
                list.add(value);
            }
        }

        int ans = 0;

        for(int num: list){
            ans+=num;
        }

        return ans;

        
    }
}