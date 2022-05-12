# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        uf = {} #node: parent
        nodes = {}
        
        def dfs(parent, node, uf, nodes):
            if node:
                uf[node.val] = parent
                nodes[node.val] = node
                dfs(node, node.left, uf, nodes)
                dfs(node, node.right, uf, nodes)
        
        dfs(root, root, uf, nodes)
        
        pParents = []
        while p.val != root.val:
            pParents.append(p.val)
            p = uf[p.val]
        pParents.append(root.val)
                
        qParents = []
        while q.val != root.val:
            qParents.append(q.val)
            q = uf[q.val]
        qParents.append(root.val)
            
        print(pParents)
        print(qParents)
                
        for p in pParents:
            if p in qParents:
                return nodes[p]        
        