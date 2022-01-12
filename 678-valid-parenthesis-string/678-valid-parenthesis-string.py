class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        for char in s:
            if char == '(':
                low +=1 
                high +=1 
            elif char == ')':
                low -= 1
                high -= 1 
            else:
                low -= 1 
                high +=1
            low = max(0, low)
            if low > high:
                return False
        return low == 0