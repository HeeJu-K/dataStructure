"""
Approach: dp
on the matrix, record the steps to 0, starting from each zero. only visit above, below, left and right.
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        q = deque()
        MAX_DIS = rows*cols

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0: 
                    q.append([i,j])
                else: mat[i][j] = MAX_DIS

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                r, c = row + dr, col + dc 
                if 0<=r<rows and 0<=c<cols and mat[row][col]+1 < mat[r][c]: #within the range and next elem is not updated
                    mat[r][c] = mat[row][col]+1
                    q.append([r, c])
        return mat
