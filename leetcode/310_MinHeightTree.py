"""
Approach: BFS + dict
In order to be a Minimum Height Tree, the root node has to contain most childs
The question tells us to return all possible roots of a minimum height tree, each MHT will have one root and at most there are two roots possible,
Thus, cut the leaf nodes (or the nodes with one connection) in turns, the remaining are possible roots
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #edge case
        if n == 1: return [0]
        #dictionaries are indexed from 0 to n-1
        adj = {i:set() for i in range(n)}
        for [u, v] in edges:
            adj[u].add(v)
            adj[v].add(u)
        #leave contain values 0 to n-1 if it is a leaf
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n>2:
            tmp = []
            n-=len(leaves)
            for leaf in leaves:
                leaves = leaves[1:]
                l = adj[leaf].pop() # get index of node connected to cur leaef
                adj[l].remove(leaf) # remove cur leaf from node's connected neighbors
                # if node becomes leaf node, append to result at last. 
                ##this is because when leaf are cut, 
                ##the remainings are roots and we do not wish to cut more
                if len(adj[l]) == 1:
                    tmp.append(l)
            leaves = tmp
        return leaves