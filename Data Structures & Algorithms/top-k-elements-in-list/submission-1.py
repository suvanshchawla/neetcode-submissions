class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Need to find the k-most frequent elements
        # Create a frequency counter first
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res


        