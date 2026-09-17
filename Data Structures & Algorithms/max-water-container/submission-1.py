class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to find the container that can hold most amount of water
        # max water that any 2 bars can store would be area, (index_right - index_left) * min(array[left], array[right])
        # Can use 2 pointers again for this
        # start from left and right and calculate the amount of water they can store
        # need to find the strategy to move the pointers
        # if left < right, then move left else move right, because the smaller height can hold the water only upto it's height and decreasing the width is only going to decrease the area
        left = 0
        right = len(heights) - 1
        max_vol = 0
        
        while left < right:
            curr = min(heights[left], heights[right])*(right - left)
            max_vol = max(curr, max_vol)
            # we compare the left and the right and then move the pointer, whichever one is smaller is bascially the limiting factor, because with decreasing width the area can't increase of the height, so whichever one is smaller we move ahead on that one
            if heights[left] >= heights[right]:
                right-=1
            else:
                left+=1

        return max_vol