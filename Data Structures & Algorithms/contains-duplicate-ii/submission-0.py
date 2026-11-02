class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # We can loop through all the elements
        # in the loop we look at each number
        l = 0
        count = {}

        for r in range(len(nums)):
            if r - l > k:
                count[nums[l]] -= 1
                l += 1
                
                if nums[r] in count.keys() and count.get(nums[r]) > 0:
                    return True
                count[nums[r]] = 1 + count.get(nums[r], 0)
            
            else:
                if nums[r] in count.keys() and count.get(nums[r]) > 0:
                    return True
                else:
                    count[nums[r]] = 1 + count.get(nums[r], 0)
            
        return False
