class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to find the container that can hold most amount of water
        # max water that any 2 bars can store would be area, (index_right - index_left) * min(array[left], array[right])
        # Can use 2 pointers again for this
        # start from left and right and calculate the amount of water they can store
        # need to find the strategy to move the pointers
        # if moving left increases water then left++, if moving right increases water then move right
        left = 0
        right = len(heights) - 1
        max_vol = 0
        
        while left < right:
            curr = min(heights[left], heights[right])*(right - left)
            max_vol = max(curr, max_vol)
            if heights[left] >= heights[right]:
                right-=1
            else:
                left+=1

        return max_vol