## Recursive DFS Solution for maximum depth of binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0

        def dfs(node, depth):
            if node is None:
                return max(maxdepth, depth)
            
            leftMax = dfs(node.left, depth + 1)
            rightMax = dfs(node.right, depth + 1)
            return max(leftMax, rightMax)
        
        return dfs(root, 0)
        