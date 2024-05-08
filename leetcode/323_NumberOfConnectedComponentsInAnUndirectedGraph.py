
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)

        visited = set()
        def dfs(node):
            stack = [node]
            path = []
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    visited.add(cur)
                    path.append(cur)
                    for neighbor in d[cur]:
                        stack.append(neighbor)
                    
            return path
        
        arr = [1]*n
        res = 0
        for i in range (n):
            if i not in visited:
                total_path = dfs(i)
                
                for j in total_path:
                    arr[j] = len(total_path)
                res += 1
        return res