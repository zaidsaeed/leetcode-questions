class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def isMatchRec(s, p):
            
            if not bool(p):
                return not bool(s)
            
            firstMatch = bool(s) and p[0] in {'.', s[0]}
            
            if len(p) >= 2 and p[1] == '*':
                return (firstMatch and isMatchRec(s[1:], p)) or (isMatchRec(s,p[2:]))
            else:
                return firstMatch and isMatchRec(s[1:], p[1:])
        
        return isMatchRec(s, p)
        
        