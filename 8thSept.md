Prob: https://leetcode.com/problems/increasing-order-search-tree/submissions/

Soln:

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = res = TreeNode(None)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.aux(root)
        return self.res.right

    def aux(self, root):
        if root:
            self.aux(root.left)
            self.ans.right = TreeNode(root.val)
            self.ans = self.ans.right
            self.aux(root.right)
            return self.res


```
