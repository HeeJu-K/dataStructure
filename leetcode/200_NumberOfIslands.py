class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        print(m, n)
        cnt = 0

        def connect(grid, i, j, m, n):
            if i<m and j<n and i>=0 and j>=0 :
                if grid[i][j] == "1":
                    grid[i][j] = "2"
                    connect(grid, i-1, j, m, n)
                    connect(grid, i+1, j, m, n)
                    connect(grid, i, j-1, m, n)
                    connect(grid, i, j+1, m, n)
            return

        for i in range (m):
            for j in range (n):
                if grid[i][j] == "1":
                    cnt += 1
                    connect(grid, i, j, m, n)
        return cnt