class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            char = s[i]
            count += 1
            center = i
            inc = 1
            while (center-inc >= 0 and center+inc < len(s)):
                if s[center-inc] == s[center+inc]:
                    count += 1
                    inc += 1
                else:
                    break
            
            lC, rC = i, i+1
            if i+1 < len(s) and s[lC] == s[rC]:
                count += 1
                inc = 1
                while (lC-inc >= 0 and rC+inc < len(s)):
                    if s[lC-inc] == s[rC+inc]:
                        count += 1
                        lC -= 1
                        rC += 1
                    else:
                        break
            
        return count