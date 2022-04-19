class Solution:
    def isPalindrome(self, s: str) -> bool:
        fS = ''
        for char in s:
            if char.isalnum():
                fS += char.lower()
        
        b, e = 0, len(fS) - 1
        ans = True
        while (b <= e):
            if fS[b] != fS[e]:
                return False
            b += 1
            e -= 1
        
        return ans
        