class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shorter, longer = None, None
        if len(s) != len(t):
            return False
        else:
            shorter = s
            longer = t
        
            def getCharArr(string):
                charArr = [0 for i in range(26)]
                for char in string:
                    index = ord(char) - ord('a')
                    charArr[index] += 1
                return charArr

            shorterArr = getCharArr(shorter)
            longerArr = getCharArr(longer)

            for i in range(len(shorterArr)):
                if shorterArr[i] != longerArr[i]:
                    return False
            return True