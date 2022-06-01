# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot):
            return True
        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
        
    def isMatch(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root:
            return False
        if not subRoot:
            return False
        if root and subRoot:
            if root.val == subRoot.val:
                return self.isMatch(root.left, subRoot.left) and self.isMatch(root.right, subRoot.right)
        return False
    
    ''