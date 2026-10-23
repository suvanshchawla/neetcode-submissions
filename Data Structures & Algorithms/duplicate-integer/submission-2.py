# This can be done with a hashmap or a dictionary

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_nums = {}

        for num in nums:
            if num not in list_nums:
                list_nums[num] = num
            else:
                return True
        return False