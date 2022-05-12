# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pVal = min(p.val, q.val)
        qVal = max(p.val, q.val)
        return self.lcaRec(root, pVal, qVal)
        
    def lcaRec(self, root, p, q):
        if root.val >= p and root.val <= q:
            return root
        elif root.val > p and root.val > q:
            return self.lcaRec(root.left, p, q)
        else:
            return self.lcaRec(root.right, p, q)
            
        