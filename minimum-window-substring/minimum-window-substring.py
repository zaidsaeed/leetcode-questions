class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        ans = [0, 0, float('inf')]
        charMap = self.createCharMap(t)
        windowCharMap = {}

        while ((l < len(s)) and (r < (len(s) + 1))):
            window = s[l:r]
            if (self.isProperSubset(window, charMap, windowCharMap)):
                if (ans[-1] > len(window)):
                    ans = [l, r, len(window)]
                windowCharMap[s[l]] = windowCharMap[s[l]] - 1
                if windowCharMap[s[l]] == 0:
                    del windowCharMap[s[l]]
                l += 1
            else:
                
                if r < len(s):
                    if (s[r] in windowCharMap):
                        windowCharMap[s[r]] = windowCharMap[s[r]] + 1
                    else:
                        windowCharMap[s[r]] = 1
                r += 1
        return s[ans[0]: ans[1]]
    
    def isProperSubset(self, window, charMap, windowCharMap):
        for key in charMap.keys():
            if (not key in windowCharMap) or windowCharMap[key] < charMap[key]:
                return False
        return True
    
    def createCharMap(self, t):
        charMap = {}
        for char in t:
            if char in charMap:
                charMap[char] = charMap[char] + 1
            else:
                charMap[char] = 1
        return charMap