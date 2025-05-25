def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #in-order: left -> root -> right 
        #recursive impl 
        res = []

        def dfs(node):
            if node is None:
                return 
                
            if node.left: 
                dfs(node.left)
            
            res.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        return res 