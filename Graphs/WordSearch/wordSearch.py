class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                if dfs(i+x, j+y, k+1):
                    return True

            board[i][j] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False