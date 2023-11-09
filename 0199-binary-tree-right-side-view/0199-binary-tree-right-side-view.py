# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.max_level = -1
        self.result = []
        def rec(root, level):
            if not root:
                return
            if level > self.max_level:
                self.result.append(root.val)
                self.max_level = level

            rec(root.right, level + 1)
            rec(root.left, level + 1)

        rec(root, 0)
        
        return self.result