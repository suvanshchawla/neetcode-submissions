class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}
        for i, num in enumerate(nums):

            required = target - num
            if required in sums:
                return [sums[required], i]
            else:
                sums[num] = i
        
        return [-1, -1]