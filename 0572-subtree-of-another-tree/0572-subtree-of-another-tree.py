# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtreeRec(root, subRoot, False)
        
    def isSubtreeRec(self, root, subRoot, isMatch):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        elif (root.val == subRoot.val):
            if self.isSubtreeRec(root.left, subRoot.left, True) and self.isSubtreeRec(root.right, subRoot.right, True):
                return True
        if isMatch:
            return False
        else:
            return self.isSubtreeRec(root.left, subRoot, False) or self.isSubtreeRec(root.right, subRoot, False)
        
        
        '''
            (3,3)
                A(1,4)
                (2,5)
        
        '''