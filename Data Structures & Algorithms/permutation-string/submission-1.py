# should we find different permutations of a string?
# That could be a long process
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # we have a fix length of s1 that needs to be searched in s2

        # Create a freq map of s1
        freq_s1 = [0]*26
        freq_s2 = [0]*26

        for char in s1:
            idx = ord(char) - ord('a')
            freq_s1[idx]+=1
        
        for i in range(len(s2)):
            idx = ord(s2[i]) - ord('a')
            if i >=len(s1):
                letter = i - len(s1)
                freq_s2[ord(s2[letter]) - ord('a')]-=1
                
            freq_s2[idx]+=1
            
            if freq_s1 == freq_s2:
                return True
        
        return False
            

