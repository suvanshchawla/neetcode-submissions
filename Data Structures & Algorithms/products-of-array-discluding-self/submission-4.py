class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to remember that the zeros can screw the product: if there is 1 zero then only the the index of the zero will have the value if there are more than 1 0 then the entire thing will be 0
        # We can try this prefix/suffix solution where we can create 2 arrays, prefix and suffix, which will hold the prefix (product of nums till ith index) and suffix (product of nums after i till end) for each index i and multiply them
        n = len(nums)
        prefix = n*[0]
        suffix = n*[0]
        res = n*[0]

        prefix[0] = suffix[n -1] = 1

        for i in range(1, n):
            prefix[i] = prefix[i -1]*nums[i -1]
        for i in range (n - 2, -1, -1):
            suffix[i] = suffix[i + 1]* nums[i + 1]
        for i in range(n):
            res[i] = prefix[i]*suffix[i]
        
        return res



            
            