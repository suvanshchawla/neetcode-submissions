class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if we sort this, and then think?
        # Input: nums = [-1,0,1,2,-1,-4]
        # sorted nums = [-4, -1, -1, 0, 1, 2]
        # For the numbers to add to 0 we need negative numbers
        res = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    res.append([val, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
        return res

        