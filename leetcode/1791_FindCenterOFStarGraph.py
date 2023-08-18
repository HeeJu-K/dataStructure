"""
Intuitive Approach: Store the sums of connections for each node, find the node with n connections
Second Approach: Since it's a star, every nodes are connected to the center node and center node to every node. Only check the first two instance as n>2
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        ENHANCED APPROACH
        center is either the first or not.
        Only [0][0] or [0][1] can be the answer
        """
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]: return edges[0][0]
        else: return edges[0][1]
        """
        FIRST APPROACH
        # there are n-1 edges in total, therefore n ndoes
        n = len(edges)+1
        # now n denotes the number of nodes, from 0 to n-1
        sums = [0]*(n)
        #edge case: there are always more than 3 nodes
        # print("init", sums, n)
        for [u, v] in edges:
            print("for", u, v)
            sums[u-1] +=1
            sums[v-1] += 1
        #     print("sums", sums)
        # print('final', sums)
        for i in range(1, n+1):
            # print("res", sums[i-1], i, n)
            if sums[i-1] == n-1:
                return i
        return -1
        """
        