"""
Approach: Dijkstra
"""
from queue import PriorityQueue

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        # efforts store the min effort to the node, heights store the actual height of the node
        efforts = [[float("inf") for _ in range (cols)] for _ in range(rows)]
        efforts[0][0] = 0
        pq = [(0,0,0)]

        while pq:
            # pop the node with smallest distance
            effort, x, y = heapq.heappop(pq)
            # check if reached the end
            if x == rows-1 and y == cols-1:
                return effort
            for dx, dy in dirs:
                X, Y = x+dx, y+dy

                if 0<=X<rows and 0<=Y<cols:
                    # update efforts to current min_efforts
                    new_effort = max(effort, abs(heights[X][Y] - heights[x][y]))
                    if new_effort < efforts[X][Y]:
                        efforts[X][Y] = new_effort
                        heapq.heappush(pq, (new_effort, X, Y))
                    
