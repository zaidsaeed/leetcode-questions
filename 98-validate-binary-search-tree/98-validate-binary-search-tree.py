# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBSTRec(root, maxVal, minVal):
            if root:
                rootVal = root.val
                leftVal = float('-inf')
                if root.left:
                    leftVal = root.left.val
                rightVal = float('inf')
                if root.right:
                    rightVal = root.right.val
                
                if rootVal < rightVal and rootVal > leftVal:
                    if rootVal > minVal and rootVal < maxVal:
                        return isValidBSTRec(root.left, root.val , minVal) and isValidBSTRec(root.right, maxVal, root.val)
                return False
            
            return True
        
        return isValidBSTRec(root, float('inf'), float('-inf'))
        