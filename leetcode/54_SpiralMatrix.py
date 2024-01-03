class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        i = j = 0
        top, bottom, left, right = 0, m-1, 0, n-1
        total = m*n
        res = []
        while len(res) < total:
            for i in range (left, right+1):
                res.append(matrix[top][i])
            for j in range (top+1, bottom+1):
                res.append(matrix[j][right])
            if top != bottom:
                for i in range (right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            if left != right:
                for j in range (bottom-1, top, -1):
                    res.append(matrix[j][left])
            left += 1 
            right -= 1
            top += 1    
            bottom -= 1
            
        return res