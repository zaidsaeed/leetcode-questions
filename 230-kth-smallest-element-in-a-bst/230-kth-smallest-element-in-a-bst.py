# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0

    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kRec(root, k)
    
    def kRec(self, root, k):    
        if root:
            left = self.kRec(root.left, k)
            if left is not None:
                return left
            self.count += 1
            if self.count == k:
                return root.val
            right = self.kRec(root.right, k)
            if right is not None:
                return right