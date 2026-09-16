class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are given a 2d matrix and we need to see find if the sudoku is valid or not, with standard rules of sudoku
        # it is a 9x9, so, initial approach is to do 3 types of searches all rows, all columns and then 9 boxes
        # if all them are valid then it is a valid board
        # simplest way is to use a hashtable search all rows and columns and boxes

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c //3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
