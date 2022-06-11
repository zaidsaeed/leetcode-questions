class Solution:
    
    digitMap = {
        '2': ["a","b","c"],
        '3': ["d","e","f"],
        '4': ["g","h","i"],
        '5': ["j","k","l"],
        '6': ["m","n","o"],
        '7': ["p","q","r","s"],
        '8': ["t","u","v"],
        '9': ["w","x","y","z"]
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        for digit in digits:
            if len(ans) == 0:
                ans = self.digitMap[digit].copy()
            else:
                oldAns = ans.copy()
                newAns = []
                for elem in oldAns:
                    for toAdd in self.digitMap[digit]:
                        newAns.append(elem+toAdd)
                ans = newAns
        return ans
            
        