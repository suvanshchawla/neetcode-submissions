class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are given a 2d matrix and we need to see find if the sudoku is valid or not, with standard rules of sudoku
        # it is a 9x9, so, initial approach is to do 3 types of searches all rows, all columns and then 9 boxes
        # if all them are valid then it is a valid board
        # simplest way is to use a hashtable search all rows and columns and boxes

        nums_rows = {}
        
        len_rows = len(board)
        len_cols = len(board[0])
        for i in range(len_rows):
            nums_col = {}
            for j in range(len_cols):
                value = board[i][j]
                if nums_col.get(board[i][j], 0) > 0 and board[i][j] !="." :
                    return False
                else:
                    nums_col[value] = 1
        
        for i in range(len_rows):
            nums_col = {}
            for j in range(len_cols):
                value = board[j][i]
                if nums_col.get(board[j][i], 0) > 0 and board[j][i] !="." :
                    return False
                else:
                    nums_col[value] = 1

        for b in range(9):
            nums_col = {}
            row_start = (b // 3) * 3
            col_start = (b % 3) * 3
            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    value = board[r][c]
                    if nums_col.get(value, 0) > 0 and value != ".":
                        return False
                    nums_col[value] = 1


        # now we need to run the loop for 3x3 times 9
        # First time we 


        
        return True