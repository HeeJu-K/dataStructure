"""
Approach: BFS
Ans = Neighbors of City 1 + Neighbors of City 2 - 1 (if City 1&2 are connected)
dictionary, queue, max, neighbor1 , neighbor2
Approach 2: no BFS? O(n)
dictionary store neighbors,
for loop iterate each node length, `in` to check if connected
find max lengths from dictionary
EDGE CASE: three nodes have same number of neighbors, where two are connected -> Should not -1 but it might
->bfs to mark neighbors and calculate 

"""
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        elif len(roads) == 1: return 1
        d = {i:set() for i in range (n)}
        for [a, b] in roads:
            d[a].add(b)
            d[b].add(a)

        max1 = [[len(d[0]), 0]]
        max2 = [min([len(d[0]), 0], [len(d[1]), 1], key= lambda p: p[0])]
        for i in range (1,n):
            neighbors = len(d[i])
            if len(max1) and neighbors>max1[-1][0]:
                max2 = max1
                max1 = [[neighbors, i]]
            elif len(max1) and neighbors == max1[-1][0]: # numbers are duplicate
                max1.append([neighbors, i])
            elif len(max2) and neighbors>max2[-1][0]:
                max2=[[neighbors,i]]
            elif len(max2) and neighbors == max2[-1][0]: max2.append([neighbors,i])

        res = 0
        if len(max1)>=2: max2 = max1
        for i in range (len(max1)):
            for j in range (i, len(max2)):
                if max2 == max1 and i==j: continue
                res = max(max1[i][0]+max2[j][0]-1 if max2[j][1] in d[max1[i][1]] else max1[i][0]+max2[j][0], res)
        return res