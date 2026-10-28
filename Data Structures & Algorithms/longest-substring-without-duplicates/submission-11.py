class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We need to find the longest substring that doesn't repeat itself
        res = 0
        
        seen = {}
        l = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]]+1, l)
            seen[s[r]] = r
            res = max(res, r-l+1)
        return res
        