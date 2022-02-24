from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        if len(nums) <= 1:
            return count
        even, odd = [], []
        for i in range(0, len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        evenMap = Counter(even)
        oddMap = Counter(odd)
        evenChar, evenCount, evenChar2, evenCount2 = self.mostFreq(evenMap)
        oddChar, oddCount, oddChar2, oddCount2 = self.mostFreq(oddMap)
        print(evenMap)
        print(evenChar)
        print(evenCount)
        print(evenChar2)
        print(evenCount2)
        if oddChar != evenChar:
            sum1 = len(odd) - oddCount
            sum2 = len(even) - evenCount
            return sum1 + sum2
        else:
            sum1 = len(even) - evenCount #1
            sum2 = len(odd) - oddCount2 # 3
            res1 = sum1 + sum2 # 4
            sum3 = len(even) - evenCount2 #3
            sum4 = len(odd) - oddCount #0
            res2 = sum3 + sum4 #3
            return min(res1, res2) 
        
    def mostFreq(self, intMap):
        maxChar, maxCount = None, 0
        secMaxChar, secMaxCount = None, 0
        for (char, count) in intMap.items():
            if count > maxCount:
                secMaxChar = maxChar
                secMaxCount = maxCount
                maxChar = char
                maxCount = count
            elif count > secMaxCount:
                secMaxChar = char
                secMaxCount = count
        return maxChar, maxCount, secMaxChar, secMaxCount

#[4, 4, 3]
#[4, 4, 4]
        