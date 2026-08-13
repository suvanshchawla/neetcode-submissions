class Solution {
    public int removeElement(int[] nums, int val) {
        int whereToAdd = 0;
        int notVal = 0;
    
        for(int i = 0; i<nums.length; i++){
            if(nums[i] != val){
                nums[whereToAdd] = nums[i];
                whereToAdd++;
                notVal++;
                
            }
        }

        return notVal;
    }
}