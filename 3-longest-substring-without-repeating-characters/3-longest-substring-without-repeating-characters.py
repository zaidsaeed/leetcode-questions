class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap, ans = {}, 0
        i, j = 0, 0
        while i < len(s) and j < len(s):
            newChar = s[j]
            if not newChar in charMap or charMap[newChar] < i:
                charMap[newChar] = j
            else:
                i = charMap[newChar] + 1
                charMap[newChar] = j
            ans = max(ans, (j-i+1))
            j += 1
        return ans
    
    '''
    charMap = {
        t: 0,
        m: 2,
        z: 3,
    }
    ans = 2
    
    "t m m  z u x t"
         i  j
    
    '''