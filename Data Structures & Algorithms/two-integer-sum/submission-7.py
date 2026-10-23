# another easy problem I think it can be solved using 2 ways - 2 ptrs or keeping the remainder from the current num as key and index as the value
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list_sum = {}
        
        for idx in range(0, len(nums)):
            remainder = target - nums[idx]
            if remainder in list_sum:
                return [list_sum[remainder], idx]
            else:
                list_sum[nums[idx]] = idx
        
        return [-1, -1]

# [3, 4, 5, 6] -> idx = 0 remainder = 7 - nums[0] = 7 - 3 = 4. -> list_sum[4] = 0,
# idx = 1 remainder = 7 - 4 = 3   