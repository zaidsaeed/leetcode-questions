class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
                        (((   )))
            
                            (
                        ((          ()
                    (((   (()     ()( ())
        
        '''
        
        # (open, closed, str)
        arr = [[1, 0, '(']]
        ans = []
        
        while arr:
            elem = arr.pop()
            # add closing parenthesis
            elemPC = elem.copy()
            elemPC[1] += 1
            elemPC[2] += ')'
            
            if elemPC[0] == n and elemPC[1] == n:
                ans.append(elemPC[2])
            elif (elemPC[0] >= elemPC[1]) and elemPC[0] <= n and elemPC[1] <= n:
                arr.append(elemPC)
            
            # add opening paranthesis
            elemPO = elem.copy()
            elemPO[0] += 1
            elemPO[2] += '('
            
            if elemPO[0] == n and elemPO[1] == n:
                ans.append(elemPO[2])
            elif (elemPO[0] >= elemPO[1]) and elemPO[0] <= n and elemPO[1] <= n:
                arr.append(elemPO)
        
        return ans