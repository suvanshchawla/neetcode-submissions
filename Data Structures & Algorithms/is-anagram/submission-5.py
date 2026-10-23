# This can be done easily with a dictionary too I think
# The idea could be to create a dictionary and add one 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dict_of_letters = {}

        for char in s:
            dict_of_letters[char] = dict_of_letters.get(char, 0) + 1

        for char in t:
            dict_of_letters[char] = dict_of_letters.get(char, 0) - 1

        
        for key in dict_of_letters:
            if dict_of_letters[key] != 0:
                return False
        
        return True



        
