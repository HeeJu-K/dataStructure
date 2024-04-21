"""
DFS 
Go to the bottom of a farmland then the rightmost end of a farmland
1 0 1 1 1 0 1 
1 0 1 1 1 0 0
1 0 1 1 1 0 0
0 0 0 0 0 

Edge Cases

Another approach: If allowed to change the matrix, store the length of the farmland.
Assume we are always exploring from the left to right of the matrix, add the number of the value stored in array, to skip the farmland if it exists
"""

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        visited = set()
        result = []

        def dfs(i,j):
            visited.add((i,j))
            
            if i+1<rows and land[i+1][j] and land[i+1][j] not in visited:
                return dfs(i+1, j)
            if j+1<cols and land[i][j+1] and land[i][j+1] not in visited:
                return dfs(i, j+1)
            if i+1>=rows or land[i+1][j] == 0:
                return (i,j)
            if j+1>=cols or land[i][j+1] == 0:
                return (i,j)


        for row in range(rows):
            for col in range(cols):
                if land[row][col] and (row, col) not in visited:
                    bottom, _ = dfs(row, col)
                    _, right = dfs(row, col)
                    for i in range (row, bottom+1):
                        for j in range (col, right+1):
                            visited.add((i,j))
                    result.append([row, col, bottom, right])

        return result
                
        