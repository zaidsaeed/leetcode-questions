# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
      	
        def checkTargetSumRec(root, target, count):
            if not root:
                return False
            if target == (count + root.val):
                if not root.right and not root.left:
                    return True
            return checkTargetSumRec(root.left, target, count + root.val) or checkTargetSumRec(root.right, target, count + root.val)
        
        return checkTargetSumRec(root, targetSum, 0)
  
        