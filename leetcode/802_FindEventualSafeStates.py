"""
Approach: BFS
d: Reverse list of Directed Graph
q: keep track of valid nodes connected to terminal
Start from the terminal node, bfs to cut out the leaf 
If a node does not have out_degrees, it means it has single route to terminal, return those nodes
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # create dict with prev nodes of each nodes
        d = {i:[] for i in range(n)}
        for i, val in enumerate(graph):
            for v in val:
                d[v].append(i)

        out_degrees = {i: len(val) for i, val in enumerate(graph)}
        # initialize q with terminal nodes
        q = deque(i for i in range(n) if not graph[i])

        visited = set()

        while q:
            node = q.pop()
            
            for neighbor in d[node]:
                out_degrees[neighbor] -= 1
                if out_degrees[neighbor] == 0 and neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                
        return [i for i in range(n) if out_degrees[i] == 0]

