# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, samenode):
            if not node and not samenode:
                return True
            if not node or not samenode:
                return False
            if node.val != samenode.val:
                return False
                
            left = dfs(node.left, samenode.left)
            right = dfs(node.right, samenode.right)
            return (left and right)

        return dfs(p, q)
            