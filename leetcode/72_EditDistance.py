class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range (l2+1)] for _ in range (l1+1)]
        for i in range (max(l1, l2)+1):
            if i <= l1:
                dp[i][0] = i
            if i <= l2:
                dp[0][i] = i
        print(dp)
        for i in range (1, l1+1):
            for j in range (1, l2+1):
                equal = dp[i-1][j-1] if word1[i-1] == word2[j-1] else dp[i-1][j-1]+1
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, equal)
        return dp[l1][l2]