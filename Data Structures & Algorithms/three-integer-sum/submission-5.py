class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # what do we do for the repeat part?

        res = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and nums[i-1] == val:
                continue
            
            l = i+1
            r = len(nums) - 1

            while(l<r):
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        
        return res



# [-1, 0, 1, 2, -1, -4]



        