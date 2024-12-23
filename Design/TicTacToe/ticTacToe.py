class TicTacToe:

    def __init__(self, n: int):
        #make a nxn board 
        self.board = [[0]*n for i in range(n)]
        self.n = n

    def check_horizontal(self, rowID: int, playerID: int) -> bool:
        for i in range(self.n):
            if self.board[rowID][i] != playerID:
                return False

        return True
    
    def check_vertical(self, colID: int, playerID: int):
        for i in range(self.n):
            if self.board[i][colID] != playerID:
                return False
        
        return True

    def check_left_diagonal(self, playerID: int):
        for i in range(self.n):
            if self.board[i][i] != playerID:
                return False
        return True

    def check_right_diagonal(self, playerID: int):
        for i in range(self.n):
            if self.board[i][self.n-i-1] != playerID:
                return False
        return True
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if self.check_horizontal(row, player) or self.check_vertical(col, player) or self.check_left_diagonal(player) or self.check_right_diagonal(player):
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)