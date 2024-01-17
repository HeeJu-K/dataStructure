class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # has to be more than 101 rows, hence more than 102 cols
        dp = [[0]*k for k in range (1, 102)]
        dp[0][0] = poured
        for i in range(query_row+1):
            for j in range (i+1):
                flow = (dp[i][j] - 1)/2
                if flow > 0:
                    dp[i+1][j] += flow
                    dp[i+1][j+1] += flow

        return min(1, dp[query_row][query_glass])