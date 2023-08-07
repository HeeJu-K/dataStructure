"""
Approach: binsearch, treat 2d array like a 1d array
item [i][j] = [i*n+j]
1d -> 2d
k ->  i = k//n, j = k%n
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print("testcase", matrix, target)
        m = len(matrix) # num row
        n = len(matrix[0]) # num col
        l = m*n-1
        def binSearch(start, end):
            # print("bin search", start, end)
            if start>end: return False
            mid = (start+end)//2
            i = mid//n
            j = mid%n
            # print("index: ", i, j)
            if target > matrix[i][j]:
                return binSearch(mid+1, end)
            elif target < matrix[i][j]:
                return binSearch(start, mid-1)
            else: return True
        return binSearch(0, l)
