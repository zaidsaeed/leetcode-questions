from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tCounter = Counter(t)
        for i in range(len(s)):
            sChar = s[i]
            if not sChar in tCounter:
                return False
            else:
                tCounter[sChar] -= 1
                if tCounter[sChar] == 0:
                    del tCounter[sChar]
        
        return True