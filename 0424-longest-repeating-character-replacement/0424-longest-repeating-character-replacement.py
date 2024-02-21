class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = [0 for i in range(26)]
        ans = 0
        newR = True
        while (r < len(s)):
            if newR:
                char = s[r]
                index = ord(char) - 65
                counts[index] += 1
            subStrLen = r - l + 1
            # print('    ')
            # print('----')
            # print(s[l:r+1])
            # print(max(counts))
            # print(subStrLen - max(counts))
            # print('----')
            # print('    ')
            if (subStrLen - max(counts)) > k:
                charToDecrease = s[l]
                # print("Char to decrease")
                # print(charToDecrease)
                indexToDecrease = ord(charToDecrease) - 65
                # print("indexToDecrease")
                # print(indexToDecrease)
                counts[indexToDecrease] = counts[indexToDecrease] - 1
                # print("counts[indexToDecrease]")
                # print(counts[indexToDecrease])
                l += 1
                newR = False
            else:
                r += 1
                ans = max(ans, subStrLen)
                newR = True

        return ans
                
            
            
        
'''
ABABC

A

AB

ABA

ABAB

ABABC
{
A: [0, 2],
B: [1, 3],
C: [4]
}
AAXXXAXXXAA
 ^        ^


[1, 2, 6, 10, 11] k=3
where can k numbers be placed in order to get the longest consecutive set of numbers?
[0,3,3,0]
'''