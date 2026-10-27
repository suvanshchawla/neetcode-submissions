class Solution:
    def trap(self, height: List[int]) -> int:
        # The bottleneck would be the shorter wall so that's the most amount of water that can be stored in that position anyway, and thinking of that we can move inwards

        l = 0
        r = len(height) - 1
        total_water = 0

        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
            
        return total_water

            
# [0,2,0,3,1,0,1,3,2,1]
# i in 0 - 9
# 

        


        