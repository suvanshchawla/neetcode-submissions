class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if we sort this, and then think?
        # Input: nums = [-1,0,1,2,-1,-4]
        # sorted nums = [-4, -1, -1, 0, 1, 2]
        # The problem is like 2 sum that we need to solve for any given current val at index i will be n^2 soln
        # Have to take care of the duplicates too on the left side, as we don't want it to be part of 
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0: 
                break
            
            if i > 0 and nums[i - 1] ==  val:
                continue

            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                

        return res

        