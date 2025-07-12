"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        """
        Use DFS to recursively construct the quad tree. 
        Base Case: In the case that we reach a situation where every single value in the grid is the same then we create a Node() with isLeaf = True. 
        Recursive Cases: do recursion on top left, top right, bottom left, bottom right and reduce n by half everytime.
        """

        def dfs(n, r, c):
            allSame = True 

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        #not same, set allSame to False 
                        allSame = False 

            if allSame:
                return Node(grid[r][c], True) #implcitly assume that pointers are None 

            #recursive cases 
            n = n//2 #reduce n by half
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            botLeft = dfs(n, r + n, c)
            botRight = dfs(n, r + n, c + n)

            #make non-leaf node 
            return Node(0, False, topLeft, topRight, botLeft, botRight)
        
        n = len(grid)
        r, c = 0, 0 

        return dfs(n, r, c)