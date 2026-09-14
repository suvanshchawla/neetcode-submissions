class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can sort them and store them - it is an mlogm times number of inputs - n
        listAnagram = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] +=1
            listAnagram[tuple(count)].append(word)
        return list(listAnagram.values())