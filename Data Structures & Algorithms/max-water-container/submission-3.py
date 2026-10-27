class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Given an array of heights, need to find out how much water can we store at most

        The idea is the maximum amount of water that can be stored is the area between the towers
        times the height of the shorter bar
        We can't store any water before 0th and after n-1th so we should iterate between those

        Can create a left and a right pointer, left starts from 0th and right starts from 1
        
        Calculate the area based on min(heights[l], heights[r])*(r-l)

        Now we have to decide how to move the pointers

        I think we can keep on moving the right one and decide on if we want to move the left, if it benefits us

        And we need to keep l < r

        I think we should only move the pointer with the smaller height

        Input: height = [1,7,2,5,4,7,3,6]

        l = 1
        r = 7
        area = 1



        """

        l = 0
        r = len(heights) - 1
        max_area = 0

        

        while l < r:
            curr_area = min(heights[l], heights[r])* (r-l)
            max_area = max(curr_area, max_area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        
        return max_area


