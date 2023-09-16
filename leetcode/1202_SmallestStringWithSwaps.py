"""
Approach: UF O(nlogn)
think of strings as a graph, only the linked (store in pairs) can be switched, so sort them
"""

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        else:
            return x
    def union(self, u, v):
        uu = self.find(u)
        vv = self.find(v)
        if uu != vv:
            if self.rank[uu] < self.rank[vv]:
                self.parent[uu] = vv
            else:
                self.parent[vv] = uu
                if self.rank[uu] == self.rank[vv]:
                    self.rank[uu] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UF(n)
        for u, v in pairs:
            uf.union(u, v)
        
        d = defaultdict(list)
        for idx, node in enumerate(s):
            d[uf.find(idx)].append(idx)

        # by now d stores parent node as keys and their childrens (its indices) as values
        # now, have to find parents for each char in string, sort the childrens and replace them
        res = list(s) # turn str to list
        for key in d.keys():
            indices = d[key]
            strings = [s[idx] for idx in indices] # find values of indices to sort on
            strings.sort()

            for i, c in zip(indices, strings): # zip the original indices and sorted chars
                res[i] = c
        return "".join(res)