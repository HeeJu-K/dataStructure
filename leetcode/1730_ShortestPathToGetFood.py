class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        q = deque()
        visited = set()
        dirs = ((0,1), (1, 0), (0, -1), (-1, 0))
        for i in range (n):
            for j in range (m):
                if grid[i][j] == "*":
                    q.append((0, i, j))
                    break
        while q:
            dist, x, y = q.popleft()
            for dx, dy in dirs:
                
                if 0<=x+dx<n and 0<=y+dy<m:
                    if grid[x+dx][y+dy] == "#":
                        return dist+1
                    if grid[x+dx][y+dy] == "O" and (x+dx, y+dy) not in visited:
                        visited.add((x+dx, y+dy))
                        q.append((dist+1, x+dx, y+dy))
        return -1