class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        SortedList = []
        for i, num in enumerate(nums):
            SortedList.append([num, i])
        
        SortedList.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            sum = SortedList[left][0] + SortedList[right][0]
            if sum == target:
                return [min(SortedList[left][1], SortedList[right][1]), 
                max(SortedList[left][1], SortedList[right][1])]
            elif sum < target:
                left+=1
            else:
                right-=1
        return []
