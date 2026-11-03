class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0]*26
        freq_s2 = [0]*26
        matches = 0

        if len(s1) > len(s2):
            return False

        for char in s1:
            idx = ord(char) - ord('a')
            freq_s1[idx]+=1
        
        for i in range(len(s1)):
            idx = ord(s2[i]) - ord('a')
            freq_s2[idx]+=1
        
        # Create intial matches
        for i in range(len(freq_s1)):
            if freq_s1[i] == freq_s2[i]:
                matches+=1
        
        if matches == 26:
            return True
        
        for i in range(len(s1), len(s2), 1):
            old_idx = ord(s2[i - len(s1)]) -  ord('a')
            if freq_s1[old_idx] == freq_s2[old_idx]:
                matches-=1
            freq_s2[old_idx]-=1
            
            if freq_s1[old_idx] == freq_s2[old_idx]:
                matches+=1

            new_idx = ord(s2[i]) -  ord('a')
            if freq_s2[new_idx] == freq_s1[new_idx]:
                matches-=1
            freq_s2[new_idx]+=1
            if freq_s2[new_idx] == freq_s1[new_idx]:
                matches+=1
            
            if matches == 26:
                return True
        
        return False


        