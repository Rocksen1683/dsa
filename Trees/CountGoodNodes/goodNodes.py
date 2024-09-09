# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        
        def dfs(node, currentMax):
            nonlocal goodNodes
            if currentMax <= node.val:
                goodNodes += 1

            if node.left:
                dfs(node.left, max(currentMax, node.val))

            if node.right:
                dfs(node.right, max(currentMax, node.val))

        currentMax = float("-inf")
        dfs(root, currentMax)

        return goodNodes

                