class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hasDuplicate = {}
        for num in nums:
            if num in hasDuplicate:
                return True
            else:
                hasDuplicate[num] = 0

        return False

        