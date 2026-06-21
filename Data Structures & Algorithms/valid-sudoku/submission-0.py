class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        column_set = defaultdict(set)
        grid_3x3set = defaultdict(set)

        for r in range(9):
            for c in range (9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_set[r] or board[r][c] in column_set[c] or board[r][c] in grid_3x3set[(r//3,c//3)]:
                    return False

                row_set[r].add(board[r][c])
                column_set[c].add(board[r][c])
                grid_3x3set[(r//3, c//3)].add(board[r][c])


        return True        
                