"""
Approach: 
see the choice of next possible paths as connected edges from the current edge
the problem becomes a finding shortest path in a graph question => BFS
"""
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # create an array to map coordinates with visiting sequence
        # 1: [n-1][0], 2: [n-1][1], ... 
        n = len(board)
        seq = [None] * (n**2 + 1)
        ind = 1

        cols = list(range(n))
        for row in range(n-1, -1, -1):
            for col in cols:
                seq[ind] = (row, col)
                ind += 1
            cols.reverse()

        # check if cell is already visited
        dist = [-1] * (n**2 + 1)
        dist[1] = 0

        q = deque([1])
        while q:
            cur = q.popleft()
            for i in range (cur+1, min(cur+6, n**2)+1):
                
                r, c = seq[i]
                dest = i
                if board[r][c] != -1:
                    dest = board[r][c]
                if dist[dest] == -1:
                    dist[dest] = dist[cur] + 1
                    q.append(dest)
        return dist[n**2]