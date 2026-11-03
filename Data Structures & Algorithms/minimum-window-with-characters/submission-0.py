class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Adding a simple guard before anything else
        if len(t) > len(s):
            return ""
        

        freq_t = {}
        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)

        freq_s = {}
        matches = 0

        minLen = len(s) + 1 # creating a sentinel
        minIndex = [-1,-1]
        
        l = 0
        for r in range(0 ,len(s)):
            freq_s[s[r]] = 1 + freq_s.get(s[r], 0)
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                matches+=1
            while matches == len(freq_t):
                if (r - l + 1) < minLen:
                    minIndex = [l, r]
                    minLen = r - l + 1
                
                freq_s[s[l]]-=1
                if s[l] in freq_t and freq_s[s[l]] < freq_t[s[l]]:
                    matches-=1
                l+=1
        l, r = minIndex

        return s[l:r+1] if minLen != len(s) + 1 else ""
                

            # Now we check for each character like we did in the permuations one and update minLen if the matches, match and update minIndex





        

        