# the other solution is more optimized - which is the 2 pointer approach - Depending on which wall is shorter we can find our limit/bottleneck for that side. If the left side is shorter than the right one then we can't have more water than the height of the left side of the current index, so if the left wall is short we can move inwards to see how much water we can store based on the short wall and similarly if the right wall is shorter than the current left wall then we move the left one inside
class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]

        res = 0

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res+=leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res+= rightMax - height[r]
        
        return res