class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we need to remember that the zeros can screw the product: if there is 1 zero then only the the index of the zero will have the value if there are more than 1 0 then the entire thing will be 0
        prod, cnt_zero = 1, 0
        res = [0]*len(nums)
        for num in nums:
            if num:
                prod*=num
            else:
                cnt_zero+=1
            
            if cnt_zero > 1:
                return res

        for idx, num in enumerate(nums):
            if cnt_zero:
                res[idx] = 0 if num else prod
            else:
                res[idx] = prod // num
        return res
            
            