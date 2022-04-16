# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def maxDepthRec(root, h):
            if not root:
                return 0
            if not root.left and not root.right:
                return h
            return max(maxDepthRec(root.left, h+1), maxDepthRec(root.right, h+1))
        
        return maxDepthRec(root, 1)