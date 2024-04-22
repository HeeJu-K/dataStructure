"""
BFS
# define a function that gets steps to target
define functions that get up and down steps
put states that can be reached in 1 step in queue
continue until target is reached, return -1 if queue is empty
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def increment(cur, idx):
            tmp = int(cur[idx]) + 1 if cur[idx]!="9" else 0
            return cur[0:idx] + str(tmp) + cur[idx+1:]

        def decrement(cur, idx):
            tmp = int(cur[idx]) - 1 if cur[idx]!="0" else 9
            return cur[0:idx] + str(tmp) + cur[idx+1:]

        visited = set(deadends)
        queue = deque()
        queue.append("0000")
        steps = 0

        if "0000" in visited: return -1
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target: return steps
                if cur in visited: continue
                visited.add(cur)
                for i in range(4):
                    inc = increment(cur, i)
                    if inc not in visited:
                        queue.append(inc)
                    dec = decrement(cur, i)
                    if dec not in visited:
                        queue.append(dec)
            steps += 1

        return -1