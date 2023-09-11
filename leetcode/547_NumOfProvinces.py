""" 
Approach 1: Union Find O(nlogn) 
Time Complexity O(nlogn) to iterate the adjacency matrix
-> Make an attribute to keep track of disjoint sets
Approach 2: DFS
"""
class UF:
    def __init__(self, n):
        self.parent = list(range(0, n)) # store the parent nodes of each nnodes
        self.rank = [0] * n # rank of current set
        self.num_sets = n # number of disjoint sets
    def find(self, i):
        if i == self.parent[i]:
            return i
        else: 
            return self.find(self.parent[i])
    def union(self, u, v):
        uu, vv = self.find(u), self.find(v)
        if uu != vv:
            if self.rank[uu]>self.rank[vv]:
                self.parent[vv] = uu
            else:
                self.parent[uu] = vv
                if self.rank[uu] == self.rank[vv]:
                    self.rank[uu] += 1 
                
            self.num_sets -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r = len(isConnected)
        c = len(isConnected[0])
        unions = UF(r)
        for i in range(r):
            for j in range (i, r):
                if isConnected[i][j] == 1:
                    unions.union(i, j)
        return unions.num_sets