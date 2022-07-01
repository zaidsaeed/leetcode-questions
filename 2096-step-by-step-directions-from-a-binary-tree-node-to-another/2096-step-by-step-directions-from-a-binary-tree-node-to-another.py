# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    lcaNode = None
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        uf = {}
        self.createUF(uf, root, -1, None)
        # print(uf)
        lcaNode = self.getLCA(root, uf, startValue, destValue)
        # print(lcaNode)
        return self.createString(startValue, destValue, uf, lcaNode)
    
    def createUF(self, uf, root, parent, LorR):
        if root:
            uf[root.val] = [parent, LorR]
            self.createUF(uf, root.left, root.val, 'L')
            self.createUF(uf, root.right, root.val, 'R')
    
    def getLCA(self, root, uf, startValue, destValue):
        startValParents = []
        while startValue != -1:
            startValParents.append(startValue)
            startValue = uf[startValue][0]
        
        destValParents = []
        while destValue != -1:
            destValParents.append(destValue)
            destValue = uf[destValue][0]
        
        # print(startValParents)
        # print(destValParents)
        
        for i in range(0, len(startValParents)):
            parent = startValParents[i]
            if parent in destValParents:
                return parent

    
    def createString(self, startValue, destValue, uf, lcaVal):
        string = ''
        while startValue != lcaVal:
            string += 'U'
            startValue = uf[startValue][0]
        
        downStr = ''
        while destValue != lcaVal:
            downStr = uf[destValue][1] + downStr
            destValue = uf[destValue][0]
            
        
        return string + downStr
        
    