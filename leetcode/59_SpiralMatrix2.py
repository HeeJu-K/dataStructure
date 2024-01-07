# optimized 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(n)]
        res[0][0] = 1
        item = 2
        x = y = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1,0)]
        dir_cnt = 0
        while item <= n*n:
            dx, dy = dirs[dir_cnt % 4]
            while 0 <= x+dx < n and 0 <= y+dy < n and res[x+dx][y+dy] == None:
                x += dx
                y += dy
                res[x][y] = item
                item += 1
            dir_cnt += 1
        return res

# 4 for loops 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        delta = 0
        item = 1
        res = [[None for _ in range (n)] for _ in range (n)]
        while item <= n*n:
            for i in range (delta, n-delta):
                res[delta][i] = item
                item += 1
                # print(res, delta, i, item)
            for j in range (delta+1, n-delta):
                res[j][i] = item
                item += 1
                # print(res, delta, i, j, item)
            for i in range (n-delta-2, delta-1, -1):
                res[n-delta-1][i] = item
                item += 1
                # print(res, delta, i, j, item)
            for j in range (n-delta-2, delta, -1):
                res[j][delta] = item
                item += 1
                # print(res, delta, i, j, item)
            delta += 1
        return res
    
