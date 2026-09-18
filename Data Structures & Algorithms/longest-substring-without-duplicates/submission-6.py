class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We need to find the longest substring that doesn't repeat itself
        
        if len(s) == 0:
            return 0
            
        l = 0
        r = 1
        last_seen = {}
        curr = 1
        max_len = 0

        for r in range(len(s)):
            if s[r] in last_seen and last_seen[s[r]] >= l:
                l = last_seen[s[r]] + 1
            last_seen[s[r]] = r
            max_len = max(max_len, r - l + 1)

        return max_len
            

            
        