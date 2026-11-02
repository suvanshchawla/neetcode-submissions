class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # We have a circular array - so the sum can be either in the middle -> [.(..).] or a circular warp [.)..(.]
        # if it's in the middle we can think about using similar Kadane's algorithm
        # if it is circular then we need a different approach
        # What can be done is removing the min-subarray from the middle and will be left would be the max subarray
        # find the globalMax, globalMin, currMax and currMin
        gMax, gMin = nums[0], nums[0]
        cMax, cMin = 0, 0
        total = 0

        for num in nums:
            # Decide if we want the current num to our sum or discard every thing previous to it
            cMax = max(cMax + num, num)
            
            # Similarly for cMin
            cMin = min(cMin + num, num)

            #Keeping track of the total
            total+=num

            gMax = max(cMax, gMax)
            gMin = min(gMin, cMin)
        
        # if all numbers are negative then total - cMin would give us a higher number which would 
        # -ve - (-ve) = -ve + +ve - which is inaccurate so need to check the edge case for that
        return max(gMax, total - gMin) if gMax > 0 else gMax


        


        