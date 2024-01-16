class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for string in strs:
            anagram = "".join(sorted(string))
            if anagram in anagramMap:
                anagramMap[anagram].append(string)
            else:
                anagramMap[anagram] = [string]
        return anagramMap.values()