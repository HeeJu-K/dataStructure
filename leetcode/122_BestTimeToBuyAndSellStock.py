"""
we only have to care about the next price, as there is no profit loss if we sell it multiple times
eg. 

    1 2 7 0 8

we only have to care about the next one in any cases, since 7-1 == (2-1) + (7-2)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range (len(prices)-1):
            if prices[i]<prices[i+1]:
                result += prices[i+1] - prices[i]
        return result