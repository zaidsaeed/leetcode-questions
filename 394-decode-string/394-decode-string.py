class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        charStack = []
        numStack = []
        while i < len(s):
            char = s[i]
            if char in '0123456789':
                num = s[i]
                while s[i+1] in '0123456789':
                    i += 1
                    num += s[i]
                numStack.append(int(num))
                i += 1
            elif char == ']':
                i += 1
                tempStr = ''
                temp = charStack.pop()
                while temp != '[':
                    tempStr = temp + tempStr
                    temp = charStack.pop()
                charStack.append((numStack.pop() * tempStr))
            else:
                charStack.append(char)
                i += 1
        return ('').join(charStack)
                
                    