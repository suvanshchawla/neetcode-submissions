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


// Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]

// The first student gets the sandwich
// students = [1,1,0,0,1], sandwiches = [0,0,0,1,1]

// The first student doesn't want the sandwich and goes to the end of the line
// students = [1,0,0,1,1], sandwiches = [0,0,0,1,1]

// The first student doesn't want the sandwich and goes to the end of the line
// students = [0,0,1,1,1], sandwiches = [0,0,0,1,1]

// The first student gets the sandwich
// students = [0,1,1,1], sandwiches = [0,0,1,1]

// The first student gets the sandwich
// students = [1,1,1], sandwiches = [0,1,1]

// Basically now we have the case where no one wants 0 in this line, how do we track that or in the another case
// students = [0,0,0], sandwiches = [1,0,0]

// Technically the some of lhs and rhs should be the same at all times but