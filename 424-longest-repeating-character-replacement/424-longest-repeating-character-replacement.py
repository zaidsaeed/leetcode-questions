class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s:
            l, r = 0, 0
            ans = 0
            charCnt = {}
            needChange = 0
            while (r != len(s)):
                char = s[r]
                if char in charCnt:
                    charCnt[char] += 1
                else:
                    charCnt[char] = 1
                needChange = (r - l + 1) - max(charCnt.values())
                if needChange > k:
                    charCnt[s[l]] = charCnt[s[l]] - 1
                    l += 1

                ans = max(ans, (r - l + 1))
                r += 1
                    
            return ans
   
    '''
        nC = 0
        ans = 3
        "AABABBA" k =1
         lr
    
    '''
            