class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row, loop through the array and check the duplicate

        # for column, on first row only, check the duplicate from row 1 to ro9
        for column in range(9):
            #reset the set
            column_set = set()
            row_set = set()
            for row in range(9):
                #valid row
                if board[column][row] != "." and board[column][row] in row_set:
                    return False
                row_set.add(board[column][row])
                #valid colmn 
                if board[row][column] != "." and board[row][column] in column_set:
                    return False
                column_set.add(board[row][column])

                #valid 3x3
                if row % 3 == 0 and column % 3 == 0:
                    grid_set = set()
                    for i in range(3):
                        for j in range(3):
                            if board[i+column][j+row] in grid_set and board[i+column][j+row] != ".":
                                return False
                            grid_set.add(board[i+column][j+row])
        return True







            