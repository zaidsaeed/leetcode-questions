class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        blueSoln = self.recSoln(1, red, blue, 1)
        redSoln = self.recSoln(1, red, blue, 0)
        return max(blueSoln, redSoln)
    
    def recSoln(self, level: int, red: int, blue: int, color: int) -> int:
        redLeft = (red - level) if color == 0 else red
        blueLeft = (blue - level) if color == 1 else blue
        
        if redLeft < 0 or blueLeft < 0:
            return level - 1
        nextColor = (color + 1) % 2
        return self.recSoln(level+1, redLeft, blueLeft, nextColor)