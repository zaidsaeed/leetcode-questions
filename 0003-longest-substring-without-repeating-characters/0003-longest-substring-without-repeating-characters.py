class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        ws, ans = 0, 0
        for i in range(len(s)):
            char = s[i]
            if char in lookup:
                ws = max(lookup[char] + 1, ws)
            lookup[char] = i
            ans = max(ans, (i-ws)+1)
        return ans
    
'''
    abcabcbb
       ^  ^
lookup = {
    a: 0
    b: 1
    c: 2
}
ans = 2
'''
                
                
                