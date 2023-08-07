"""
Approach1: DP
Break down into 1 node, 2 ndoes, ... , n nodes problem
Root node is chosen out of [1,n] nodes
When i is root node, [1,i) will be left subtree and (i, n] will be right subtree
the two multiplied is total number of trees
Base case: dp[0] = 0, dp[1] = 1
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        
        for i in range (1, n+1):
            for j in range (i):
                dp[i] += dp[j]*dp[i-j-1]

        return dp[n]