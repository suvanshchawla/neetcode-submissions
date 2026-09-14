class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can sort them and store them - it is an mlogm times number of inputs - n
        listAnagram = defaultdict(list)
        for word in strs:
            sorted_text = ''.join(sorted(word))
            listAnagram[sorted_text].append(word)
        return list(listAnagram.values())