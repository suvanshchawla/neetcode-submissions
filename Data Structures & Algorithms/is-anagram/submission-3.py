class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettersT = {}
        
        for char in s:
            if char in letters:
                letters[char] = letters[char] + 1
            else:
                letters[char] = 1
        
        for char in t:
            if char in lettersT:
                lettersT[char] = lettersT[char] + 1
            else:
                lettersT[char] = 1
        
        return letters == lettersT