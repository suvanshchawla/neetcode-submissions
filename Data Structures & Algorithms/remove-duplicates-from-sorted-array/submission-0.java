class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 1){
            return 1;
        }

        int curr_num = nums[0];
        int wTA = 1;
        for(int idx = 0; idx < nums.length; idx++){
            if(nums[idx] != curr_num){
                nums[wTA] = nums[idx];
                curr_num = nums[idx];
                wTA++;
            }
        }

        return wTA;
    }
}