
class Solution:
    def trap(self, height: List[int]) -> int:

        # we can try and find the max wall heigh on either side of any block
        left_side = [0]*len(height)
        right_side = [0]*len(height)

        max_height = 0
        for i in range(1, len(height)):
            max_height = max(max_height, height[i-1])
            left_side[i] = max_height
            
        
        max_height = 0
        for i in range(len(height) -2, 0, -1):
            max_height = max(max_height, height[i+1])
            right_side[i] = max_height
        
        # now we can calculate the water held at each block

        total_water = 0
        for i in range (1, len(height) - 1):
            total_water += max(0, min(left_side[i], right_side[i]) - height[i])
        
        return total_water

            


        
        