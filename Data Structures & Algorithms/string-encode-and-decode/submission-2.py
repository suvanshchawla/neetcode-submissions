class Solution:
    # The constraint is that character is a valid ascii character, the easiest way is to use a non ascii character like µ or something, other is to add some form of number and a delimiter like a # in front of it so we know what to read
    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res.append(s[i:j])
            i = j
        return res

