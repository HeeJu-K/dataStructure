"""
dp[i] = l
3 operations (dp[i+3]): 
    Ctrl A + Ctrl C + Ctrl V -> 2l
4 operations (dp[i+4]): 
    Ctrl A + Ctrl C + Ctrl V +  Ctrl V -> 3l
    A + Ctrl A + Ctrl C + Ctrl V -> 2(l+1)
5 operations (dp[i+5]): 
    Ctrl A + Ctrl C + Ctrl V + Ctrl V + Ctrl V -> 4l
       A   +    A   + Ctrl A + Ctrl C + Ctrl V -> 2(l+2)

6 operations (dp[i+6]): 
    Ctrl A + Ctrl C + Ctrl V + Ctrl V + Ctrl V + Ctrl V -> 5l
       A   +    A   +    A   + Ctrl A + Ctrl C + Ctrl V -> 2(l+3)

dp[i+3] = 2*dp[i]
dp[i+4] = 3*dp[i]
dp[i+5] = 4*dp[i]
dp[i+6] = 5*dp[i]
i+3 -> j
dp[i+7] = dp[i+3 +4] = 3*dp[i+3] = 2*3*dp[i]
"""


class Solution:
    def maxA(self, n: int) -> int:
        dp = [i for i in range (n+1)]
        for i in range (n-2):
            for j in range (i+3, min(i+6, n)+1):
                dp[j] = max(dp[j], (j-i-1)*dp[i])
        return dp[n]