class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Now let's try the bucket sort solution
        # Main Idea is to not have to sort and use the idx of a freq array as the count

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(num)
        
        return res

