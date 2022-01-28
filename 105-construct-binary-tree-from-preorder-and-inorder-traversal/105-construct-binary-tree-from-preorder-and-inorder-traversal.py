# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import OrderedDict

class Solution:
    preorderIndex = 0
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderMap = self.buildIntMap(inorder)
        left = 0
        right = len(inorder) - 1
        return self.buildTreeRec(preorder, inorder, left, right, inOrderMap)
    
    
    def buildIntMap(self, inorder):
        charMap = {}
        for i in range(len(inorder)):
            charMap[inorder[i]] = i 
        return charMap
        
    
    def buildTreeRec(self, preorder, inorder, left, right, inOrderMap):
        print(self.preorderIndex)
        if (left > right):
            return None
        val = preorder[self.preorderIndex]
        self.preorderIndex += 1
        root = TreeNode(val, None, None)
        index = inOrderMap[val]
        root.left = self.buildTreeRec(preorder, inorder, left, index - 1, inOrderMap)
        root.right = self.buildTreeRec(preorder, inorder, index + 1, right, inOrderMap)
        return root

                                

    
    