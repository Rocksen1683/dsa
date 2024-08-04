# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = [] 
        
        def inorderDFS(node):
            if not node:
                return
            inorderDFS(node.left)
            self.result.append(node.val)
            inorderDFS(node.right)
        
        inorderDFS(root)
        return self.result[k-1]
