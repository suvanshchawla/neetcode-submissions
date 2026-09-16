class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxlen = 0
        curr = 1

        
        for num in numset:
            curr = 1
            if num - 1 not in numset:
                # this is the beginning of the sequence
                curr_num = num
                while curr_num + 1 in numset:
                    curr+=1
                    curr_num = curr_num+1
            
            maxlen = max(curr, maxlen)
        
        return maxlen
                


        
# we need to find the sequence, even if it is not consecutive in the array
# simplest way is to create an enumeration and sort the array but that takes O(nlogn)
# how to find the start of the sequence?
# create a hashset and put all the numbers in it
