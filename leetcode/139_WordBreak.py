"""
Approach 1: DP
While i proceeds, go backwards until reached max length of wordDict
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # construct a dp array of n+1 size where first is always tre
        dp = [False]*(n+1)
        dp[0] = True
        
        maxword = len(max(wordDict, key=len))
        minword = len(min(wordDict, key=len))
        for i in range(n):
            for j in range(minword, maxword+1):
            
                if i-j+1>=0 and s[i-j+1:i+1] in wordDict and dp[i-j+1]:
                    dp[i+1] = True
        return dp[n]

