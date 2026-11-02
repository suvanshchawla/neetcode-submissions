class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # We have a circular array - so the sum can be either in the middle -> [.(..).] or a circular warp [.)..(.]
        # if it's in the middle we can think about using similar Kadane's algorithm
        # if it is circular then we need a different approach

        # The brute force would be to check everything
        n = len(nums)
        res = nums[0]

        for i in range(n):
            cur_sum = 0
            for j in range(i, i+n):
                cur_sum+=nums[j%n]
                res = max(res, cur_sum)
        return res


        