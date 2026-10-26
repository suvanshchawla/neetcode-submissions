class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        set_nums = set(nums)
        longest_sequence = 1

        for num in set_nums:
            curr = num
            if curr - 1 not in set_nums:
                curr_sequence = 1
                while curr + 1 in set_nums:
                    curr_sequence+=1
                    curr = curr+1
                    longest_sequence = max(longest_sequence, curr_sequence)
        

        return longest_sequence



        