"""
Approach: 
BFS through the edges and maintain two queues that can reach to each ocean
Then search if each coordinate exist in both queues
% it could use visited to differentiate delta for different oceans or could use if-elses to differentiate
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) #rows
        n = len(heights[0]) #cols
        pac_visited = [[False for _ in range(n)] for _ in range(m)]
        atl_visited = [[False for _ in range(n)] for _ in range(m)]
        pac = deque()
        atl = deque()
        res = []
        for i in range (m):
            pac_visited[i][0] = True
            pac.append([i,0])
            atl_visited[i][n-1] = True
            atl.append([i,n-1])
        for i in range (n):
            pac_visited[0][i] = True
            pac.append([0,i])
            atl_visited[m-1][i] = True
            atl.append([m-1,i])

        def bfs(q, visited):
            while q:
                [r, c] = q.popleft()
                # print("popped", r, c, q)
                for [dr, dc] in [[0,1],[0,-1],[1,0],[-1,0]]:
                    if r+dr>=0 and c+dc>=0 and r+dr<m and c+dc<n and not visited[r+dr][c+dc] and heights[r][c]<=heights[r+dr][c+dc]:
                        # print("here", r, dr, c, dc)
                        q.append([r+dr, c+dc])
                        visited[r+dr][c+dc] = True

        bfs(pac, pac_visited)
        bfs(atl, atl_visited)
        for i in range (m):
            for j in range(n):
                if pac_visited[i][j] and atl_visited[i][j]: 
                    res.append([i,j])
        return res