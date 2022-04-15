class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        
        def numDecodingsRec(string, pos):
            if pos in memo:
                return memo[pos]
            
            if pos == len(string):
                return 1
            
            oneDigit = int(string[pos:pos+1]) #1
            
            if pos == (len(string) - 1):
                if oneDigit == 0:
                    return 0
                return 1
            
            twoDigit = int(string[pos:pos+2]) #12
            way1, way2 = 0, 0
            if oneDigit != 0:
                way1 = numDecodingsRec(string, pos + 1)
                if twoDigit <= 26:    
                    way2 = numDecodingsRec(string, pos + 2)
            
            ans = way1 + way2
            memo[pos] = ans
            return ans
        
        return numDecodingsRec(s, 0)
    
    
    '''
                    226, 0
            226, 1        226,2 (1)
            
                 
                  
    
    
    
    '''