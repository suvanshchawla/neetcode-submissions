class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = n*[0]
        right_prod = n*[0]
        res = n*[0]

        left_prod[0] = right_prod[n-1] = 1

        for i in range(1, n):
            left_prod[i] = left_prod[i-1]*nums[i-1]
        for i in range(n-2, -1, -1 ):
            right_prod[i] = right_prod[i+1]*nums[i+1]
        
        for i in range(n):
            res[i] = left_prod[i]*right_prod[i]
        
        return res


            
            