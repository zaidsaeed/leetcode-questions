# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        res = []
        
        def addPath(node, path):
            if node:
                if node.left is None and node.right is None:
                    ans.append(path)
                path.append(node.val)
                addPath(node.left, path[:])
                addPath(node.right, path[:])
        
        addPath(root, [])
        
        for path in ans:
            elem = ''
            for i in range(len(path)):
                if i == 0:
                    elem += str(path[i])
                else:
                    elem += '->' + str(path[i])
            res.append(elem)
                    
        
        return res