class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int res = students.length;
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for(int student: students){
          cnt.put(student, cnt.getOrDefault(student, 0) + 1);
        }

        for(int sandwich: sandwiches){
          if(cnt.getOrDefault(sandwich, 0)> 0){
            res-=1;
            cnt.put(sandwich, cnt.get(sandwich) - 1);
          }else{
            return res;
          }
        }

        return res;

    }
}
