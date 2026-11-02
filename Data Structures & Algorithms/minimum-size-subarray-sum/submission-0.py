class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # So we start from one end 
        l = 0
        currMinLen = len(nums) + 1
        currSum = 0

        for r in range(len(nums)):
            currSum += nums[r]
            
            while currSum >=target:
                currMinLen = min(currMinLen, r - l + 1)
                currSum -=nums[l]
                l+=1
        
        return 0 if currMinLen == len(nums) + 1 else currMinLen

                # Have to write is 


            