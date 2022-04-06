class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = {}
        for word in strs:
            key = tuple(sorted(word))
            charMap[key] = charMap.get(key, []) + [word]
        return list(charMap.values())
        