# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        lvl0 = None
        lvl1 = []
        if root:
            lvl1 = [root]
        while len(lvl1) > 0:
            lvl0= lvl1
            res.append(lvl0[-1].val)
            lvl1 = []
            for node in lvl0:
                if node.left:
                    lvl1.append(node.left)
                if node.right:
                    lvl1.append(node.right)
        return res
        