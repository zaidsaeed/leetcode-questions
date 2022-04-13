class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def getStrMap(string, tMap):
            charMap = {}
            for char in string:
                if tMap and char in tMap:
                    charMap[char] = charMap.get(char, 0) + 1
                else:
                    charMap[char] = charMap.get(char, 0) + 1
            return charMap
        
        def filterS(string, tMap):
            res = []
            for i in range(len(string)):
                char = string[i]
                if char in tMap:
                    res.append((char, i))
            return res
        
        def twoMapsEqual(sMap, tMap):
            if len(sMap.keys()) != len(tMap.keys()):
                return False
            for key, val in tMap.items():
                if key not in sMap:
                    return False
                if sMap[key] < val:
                    return False
            return True
        
        tMap = getStrMap(t, None)
        filteredS = filterS(s, tMap)
        sMap = getStrMap(s, tMap)
        
        l, r = 0, 0
        ans = ''
        windowMap = {}
        done = False
        while r < len(filteredS):
            if not twoMapsEqual(windowMap,tMap):
                char = filteredS[r][0]
                windowMap[char] = windowMap.get(char, 0) + 1
                
                while l <= r and twoMapsEqual(windowMap,tMap):
                    newAns = s[filteredS[l][1]:(filteredS[r][1] + 1)]
                    if ans == '' or len(newAns) < len(ans):
                        print(newAns)
                        ans = newAns
                    windowMap[filteredS[l][0]] = windowMap[filteredS[l][0]] - 1
                    if windowMap[filteredS[l][0]] == 0:
                        del windowMap[filteredS[l][0]]
                    l += 1
                r += 1
        return ans
                
            
            
        