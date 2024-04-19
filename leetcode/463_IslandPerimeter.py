class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        visited = set()
        
        def withinRange(i, j):
            return 0<=i<rows and 0<=j<cols

        def dfs(i, j):
            nonlocal perimeter
            visited.add((i,j))
            for di,dj in dirs:
                if withinRange(i + di, j + dj) and grid[i + di][j + dj] == 1 and (i + di,j + dj):
                    if (i+di, j+dj) not in visited: dfs(i + di,j + dj)
                else:
                    perimeter += 1
                    


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter