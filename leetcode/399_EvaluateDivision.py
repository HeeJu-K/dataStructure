"""
Approach1: dfs -> visited set(), dict
-> Time complexity: O(V+E)
Approach2: use 2d array
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        l = len(queries)
        stack = []
        d = collections.defaultdict(list)
        res = []
        for i, [a, b] in enumerate(equations):
            d[a].append([b, values[i]])
            d[b].append([a, 1/values[i]])

        def dfs(start, end, visited):
            # not found
            if start not in d or start in visited: 
                return  -1
            # found the target
            if start == end: return 1
            if d[start][0] == end: 
                res[i] *= d[start][1]
                return 
            visited.add(start)
            for [neighbor, value] in d[start]:
                path = dfs(neighbor, end, visited)
                if path != -1:
                    return value*path
            return -1

        for i in range (l):
            res.append(dfs(queries[i][0], queries[i][1], set()))
        return res
