class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # let's do it the hashmap way
        # we can use the remainder of whatever is required from the target as the key and the position as the value

        sums = {}
        for i, num in enumerate(nums):
            # 0, 3 ; 1, 4 ; 2, 5 ; 3, 6
            # target = 7
            # index, number
            # required = 7 - 3 = 4
            # check for 4 in sums, if not, then {4: 0, }
            # required = 7 - 4 = 3
            # check for 3 in sums, if not, then {4: 0, 3: 1}

            required = target - num
            if required in sums:
                return [sums[required], i]
            else:
                sums[num] = i
        
        return [-1, -1]