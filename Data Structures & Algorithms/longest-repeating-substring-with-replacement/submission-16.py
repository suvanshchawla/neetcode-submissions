class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        maxF = 0
        
        l = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxF = max(maxF, seen[s[r]])

            while (r - l + 1) - maxF > k:
                seen[s[l]] -=1
                l+=1
            
            res = max(maxF, r - l + 1)
        return res



             



        