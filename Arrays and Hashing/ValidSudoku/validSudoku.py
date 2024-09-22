class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #have a hashmap of sets for cols, rows, boxes
        n = len(board)
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                
                box = str(int(i//3)*3 + int(j//3))

                if num not in rowMap[i] and num not in colMap[j] and num not in boxMap[box]:
                    rowMap[i].add(num)
                    colMap[j].add(num)
                    boxMap[box].add(num)
                else:
                    return False

        return True

