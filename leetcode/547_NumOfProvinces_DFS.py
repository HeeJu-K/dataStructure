# Approach 2 DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in range (n):
                if i!=j and isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
            return
        
        num_Provinces = 0
        for i in range (n):
            if i not in visited:
                dfs(i)
                num_Provinces+=1
        return num_Provinces