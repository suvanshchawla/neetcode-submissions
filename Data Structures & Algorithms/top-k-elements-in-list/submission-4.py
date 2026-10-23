class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Now let's try the bucket sort solution
        # Main Idea is to not have to sort and use the idx of a freq array as the count

        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1
        
        freq = [[] for _ in range(len(nums)  + 1)]
        # Now we have a frquency map - 
        # use this map to create a bucket based on the values
        # we create nums+1 empty buckets because worst case all
        # the numbers are the same and would end up in the last bucket
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

