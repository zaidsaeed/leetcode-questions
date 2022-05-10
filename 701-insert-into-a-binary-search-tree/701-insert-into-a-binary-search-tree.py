# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent = None
        pointer = root
        while pointer:
            parent = pointer
            if val > pointer.val:
                pointer = pointer.right
            else:
                pointer = pointer.left
        
        if parent:
            if parent.val > val:
                parent.left = TreeNode(val, None, None)
            else:
                parent.right = TreeNode(val, None, None)
        
        else:
            root = TreeNode(val, None, None)
        
        return root
        