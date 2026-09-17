class Solution:
    def trap(self, height: List[int]) -> int:
        # For any place we need to find the maxmium water it can hold which will be heigh[i] - min(MaxwallHeightonleft, minWallHeightonright), if the number is less than 0 we put it to zero

        if len(height) == 0:
            return 0

        #calculate the max height on the left of current idx
        max_left = [0]*(len(height))
        max_left[0] = height[0]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
        
        #calculate the max height on the right of current idx
        max_right = [0]*(len(height))
        max_right[len(height)-1] = height[len(height)-1]
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        
        # find the min of the max_left and max_right to find out the maximum water that can be held in a block
        total_water = 0
        for i in range(len(height)):
            total_water+= min(max_left[i], max_right[i]) - height[i]
        
        return total_water

            
# [0,2,0,3,1,0,1,3,2,1]
# i in 0 - 9
# 

        


        