# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            res, lvl1, lvl2 = [], [], [root]
            while lvl2:
                lvl1 = lvl2
                lvl2 = []
                for node in lvl1:
                    if node.left:
                        lvl2.append(node.left)
                    if node.right:
                        lvl2.append(node.right)
                res.append([node.val for node in lvl1])
            return res
        return []