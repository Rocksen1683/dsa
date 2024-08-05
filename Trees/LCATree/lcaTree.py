# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            #check if both p and q are greater => go right
            if (p.val > root.val) and (q.val > root.val):
                root = root.right
            #check if both p and q are smaller => go left
            elif (p.val < root.val) and (q.val < root.val):
                root = root.left
            #p and q differ => found LCA
            else:
                return root
        