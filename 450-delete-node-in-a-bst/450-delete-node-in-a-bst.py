# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
                    5
                   /  \
                  3    6
                 / \    \
                2   4    7
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root and root.val == key:
            #case 1 -> leaf node
            if not root.left and not root.right:
                return None
            
            #case 2 -> left child, no right child
            elif root.left and not root.right:
                return root.left
            
            #case 3 -> right child, no left child
            elif root.right and not root.left:
                return root.right
            
            #case 4 -> both children
            else:
                repl = self.getNextInorder(root)
                root.val = repl.val
                root.right = self.deleteNode(root.right, repl.val)
                return root
        elif root and root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root and root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

            
    def getNextInorder(self, node):
        parent = node
        node = node.right
        while node and node.left:
            parent = node
            node = node.left
        return node
            
        