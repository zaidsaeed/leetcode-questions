class Solution:
    
    def __init__(self):
        self.lessThan20 =["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        res = ''
        for i in range(0, len(self.thousands)):
            rem = num % 1000
            if rem != 0:
                res = self.helper(rem) + ' ' + self.thousands[i] + ' ' + res
            num = num // 1000
        return res.strip()
    
    def helper(self, num): #a three digit number
        res = ""
        hPlace = num // 100
        if hPlace != 0:
            res += self.lessThan20[hPlace] + ' Hundred'
        tensPlace = num % 100
        print(tensPlace)
        print(res)
        if tensPlace < 20:
            res += ' ' + self.lessThan20[tensPlace]
        else:
            onesPlace = tensPlace % 10
            tensPlace = tensPlace // 10
            res += ' ' + self.tens[tensPlace] + ' ' + self.lessThan20[onesPlace]
        return res.strip()