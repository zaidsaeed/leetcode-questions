# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        self.buildPath(root)
        return self.ans
    
    def buildPath(self, node):
        if node:
            if not node.left and not node.right:
                if node.val > self.ans:
                    self.ans = node.val
                return [[node.val], node.val]
            
            leftMaxPath = self.buildPath(node.left)
            rightMaxPath = self.buildPath(node.right)
            
            maxPath = None
            if leftMaxPath[1] >= rightMaxPath[1]:
                maxPath = leftMaxPath
            else:
                maxPath = rightMaxPath
            
            if node.val + leftMaxPath[1] + rightMaxPath[1] > self.ans:
                self.ans = node.val + leftMaxPath[1] + rightMaxPath[1]
            
            maxPath[0].append(node.val)
            maxPath[1] = maxPath[1] + node.val
            
            self.ans = max(self.ans, maxPath[1])
            
            if node.val > self.ans:
                self.ans = node.val
                
            if node.val > maxPath[1]:
                return [[node.val], node.val]
            
            return maxPath
        
        return [[], 0]
        
    
    # build path fxn. (looks at only nodes below it (left, right)) -> return path and sum
    # look at left path, right path, node 
    # return max(leftPath, rightPath, leftPath + node + rightPath, node+leftPath, node+rightPath)
        