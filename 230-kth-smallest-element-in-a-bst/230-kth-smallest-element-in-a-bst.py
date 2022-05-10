# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    ans = None
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kRec(root, k)
        return self.ans
    
    def kRec(self, root, k):    
        if root:
            self.kRec(root.left, k)
            self.count += 1
            if self.count == k:
                self.ans = root.val
                return
            self.kRec(root.right, k)