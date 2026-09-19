class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We need to find the longest substring that doesn't repeat itself
        
        if len(s) == 0:
            return 0
        l = 0
        r = 1

        seen = set()
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res, r - l + 1)
        
        return res

            

            
        