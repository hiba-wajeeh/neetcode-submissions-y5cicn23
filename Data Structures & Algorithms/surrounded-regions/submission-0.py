class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c]!='O':
                return
            
            board[r][c]='T'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        #phase 1: find unsurrounded region (O->T) (DFS)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]=='O' and (row==ROWS-1 or col==COLS-1 or row==0 or col==0):
                    dfs(row, col)

        #phase 2: capture everything thats not a T
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]=='O':
                    board[row][col]='X'

        #phase 3: change the T back to an O(T->O)
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]=='T':
                    board[row][col]='O'
