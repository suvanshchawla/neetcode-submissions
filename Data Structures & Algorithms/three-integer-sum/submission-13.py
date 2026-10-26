class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # what do we do for the repeat part?
        """
        We can start with sorting the array and creating an empty res array []

        now the idea is to search for triplets
        now that the array is sorted, we can think of fixing 1 number let's say nums[i]

        The problem talks about not duplicating triplets

        How do we solve for that?

        I think we can simply first check that the fixed number is not being repeated again

        so nums[i] != nums[i-1] have to be careful about 0th index too
        Okay now that we have checked that we can check the threeSum, if we have a fixed index
        The other part can be solved as a 2 sum II
        If the sum is greater than 0 that means the i - (left + right) > 0, so we can move the right ptr inward
        if the sum is less than 0 that would be i - (left + right) < 0, mean left+right is too small, so move 
        left ptr forward
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i+1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    # now we need to now have duplicates
                    # and if the left ptr is the same as the previous one then we might have the same ptr
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        
        return res





# [-1, 0, 1, 2, -1, -4]



        