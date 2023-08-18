"""
Approach: DFS
dictionary to store connected edges, queue and visited set for dfs
"""
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1: return True
        d = {i:set() for i in range (n)}
        print(d)
        for [u, v] in edges:
            d[u].add(v)
            d[v].add(u)
        # print("see dict", d)
        visited = set()
        q = [source]
        # print("see queue", q)
        while q:
            cur = q.pop()
            if cur == destination: return True
            visited.add(cur)
            for neighbor in d[cur]:
                if neighbor not in visited:
                    q.append(neighbor)

        return False