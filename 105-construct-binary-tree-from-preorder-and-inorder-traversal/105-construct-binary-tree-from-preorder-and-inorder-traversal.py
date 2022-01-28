# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (len(inorder) == 0 and len(preorder) == 0):
            return None
        val = preorder.pop(0)
        root = TreeNode(val, None, None)
        leftArr, rightArr, index = self.buildArr(inorder, val)
        root.left = self.buildTree(preorder[:index], leftArr)
        root.right = self.buildTree(preorder[index:], rightArr)
        return root
    
    def buildArr(self, inOrderArr, elem):
        index = 0
        for i in range(0, len(inOrderArr), 1):
            val = inOrderArr[i]
            if val == elem:
                index = i
                break
        return (inOrderArr[0:index], inOrderArr[index+1:], index)
                                

    
    