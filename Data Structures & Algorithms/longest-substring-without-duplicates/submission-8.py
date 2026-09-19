class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We need to find the longest substring that doesn't repeat itself
        
        if len(s) == 0:
            return 0
        
        map = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]] + 1, l)
            map[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
        

            

            
        