# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        elem = preorder.pop(0)
        root = TreeNode(elem, None, None)
        idx = inorder.index(elem)
        root.left = self.buildTree(preorder, inorder[0:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root

    '''
    [3,9,20]
    [9,3,20]
    
    (3)
        .left = [9,20][9] = Node(9)
                          = [20][]
                            [20][]
            
        .right = [9,20][20]
    
    Soln #1
           3
        r.left = fn([9,20,15,7], [9])
        
        
        
        
            3
          9   20
         pre=[]3,9,20
         in=[]9,3,20
         root = Node(3)
         root.left = fn([9,20], 9)
            = Node(9)
                root.left = ([20], []) = None
                root.right = ([20], []) = None
        root.right = fn([20, 15, 7], [15, 20, 7]) = Node(20)
                                       [15,7][15] = Node[15]     [15,7][7] = Node[7]
        0) if not pre or not in: return None
        1) pop out of preorder array set as elem
        2) create Node with val of elem
        3) Node.left = fn(pre, inor[:indexofelem])
        4) Node.right = fn(pre, inor[indexofelem+1:])
    '''                                        
        