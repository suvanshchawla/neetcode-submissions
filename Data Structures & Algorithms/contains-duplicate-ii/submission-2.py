class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # We can loop through all the elements
        # in the loop we look at each number
        l = 0
        count = set()

        for r in range(len(nums)):
            if r - l > k:
                count.remove(nums[l])
                l += 1
            
            if nums[r] in count:
                return True
            
            count.add(nums[r])
            
        return False
