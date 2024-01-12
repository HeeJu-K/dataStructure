from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        c_idx = 0
        stack = []
        for i in range(len(graph)):
            if i not in color:
                stack.append(i)
                color[i] = 0
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        stack.append(neighbor)
                        color[neighbor] = 0 if color[node] == 1 else 1
                    elif color[neighbor] == color[node]:
                        return False
        return True
     