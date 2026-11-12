class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We have a fixed window
        # we can find the max for the first window first and the second highest too maybe
        # Then we shift one number at a time, check if the current is bigger than the current highest
        # If so then update the highest, and make the currHighest as Second Highest
        # If not, then make the second highest as highest, then what becomes of the updatedSecondHighest, we need a way to store the a key K, and value should be the value next highest to it in the window or something like a [value, position], but that would have to be updated for all the values

        res = []

        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        
        return res