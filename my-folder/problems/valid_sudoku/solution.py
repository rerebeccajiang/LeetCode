class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # three hashmap to store the sudoku
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set) # key is (m//3, n//3)

        for m in range(9):
            for n in range(9):
                if board[m][n] == ".":
                    continue
                # check none duplication

                if(board[m][n] in row[m] or board[m][n] in col[n] or board[m][n] in grid[(m//3, n//3)]):
                    return False

                row[m].add(board[m][n])
                col[n].add(board[m][n])
                grid[(m//3, n//3)].add(board[m][n])

        return True
        