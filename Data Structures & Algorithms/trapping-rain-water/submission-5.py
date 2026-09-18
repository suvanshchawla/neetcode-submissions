class Solution:
    def trap(self, height: List[int]) -> int:
        # For any place we need to find the maxmium water it can hold which will be heigh[i] - min(MaxwallHeightonleft, minWallHeightonright), if the number is less than 0 we put it to zero

        n = len(height)
        if n == 0:
            return 0
        
        maxLeft = [0]*n
        maxRight = [0]*n

        maxLeft[0] = height[0]
        maxRight[n-1] = height[n - 1]

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        res = 0
        for i in range(n):
            res+= min(maxLeft[i], maxRight[i]) - height[i]
        
        return res

            
# [0,2,0,3,1,0,1,3,2,1]
# i in 0 - 9
# 

        


        