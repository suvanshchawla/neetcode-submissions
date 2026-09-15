class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to remember that the zeros can screw the product: if there is 1 zero then only the the index of the zero will have the value if there are more than 1 0 then the entire thing will be 0
        # We can try this prefix/suffix solution where we can create 2 arrays, prefix and suffix, which will hold the prefix (product of nums till ith index) and suffix (product of nums after i till end) for each index i and multiply them
        n = len(nums)
        res = [0]*n
        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = 1
        suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1]*prefix[i - 1]
        for i in range (n - 2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]
        
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res


            
            