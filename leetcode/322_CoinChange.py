"""
Approach: DP
initialize the DP array to amount+1, unreachable value
dp array of 0-index gets value 0
iterage through each elem in array and each coin value. 
    if dp[i-coin_val]+1 is smaller than dp[i], replace the value
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1) #initialize with unreachable maximum val
        dp[0] = 0 # 0 coin needed to make up 0 amount

        for item in range(1, amount+1):
            for coin in coins:
                if item-coin >= 0:
                    dp[item] = min(dp[item], dp[item-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1