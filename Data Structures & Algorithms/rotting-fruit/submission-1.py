class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1 
        
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        numOranges = 0

        def rotOrange(r, c):
            if (r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==2 or grid[r][c]==0):
                return 
            
            q.append([r,c])
            grid[r][c]=2

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 or grid[r][c]==2:
                    numOranges += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append([r,c])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rotOrange(r+1, c)
                rotOrange(r-1, c)
                rotOrange(r, c+1)
                rotOrange(r, c-1)
            minutes += 1
        
        minutes = max(0, minutes - 1)
        rottedOranges = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    rottedOranges += 1  

        return minutes if rottedOranges==numOranges else -1   