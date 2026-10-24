# Take a look at all the strings, find the length append the length with a separator like 4# and then read until the end the length
class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for word in strs:
            word_len = len(word)
            res+=str(word_len) + "#" + word
        return res

    def decode(self, encode_string:str) -> List[str]:

        res = []
        i = 0

        while i < len(encode_string):
            word_len = ""
            while encode_string[i] !="#":
                word_len+=encode_string[i]
                i+=1
            res.append(encode_string[i+1:i+1+int(word_len)])
            i = i+int(word_len)+1


        return res