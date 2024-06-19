"""
Approach 0: Calculate
least: ceil(n/2), max: n, every numbers between that: 2 ways
difference * 2 + 1

Approach 1: brute force
tree shape, each time add 1 or 2. If sum is equal to n, add one to answer
Time Complexity: it is a tree structure with left child always adding 1 and right child always adding 2. O(2^n)


Approach 2: memoization
remember previous step in array
TC & SC: O(n)

Approach 3: dp
either take step of 1 from 1 staircase lower or take step of 2 from 2 staircase lower
* taking 1 + 1 step from 2 staircase lower is included taking 1 step from 1 case lower
dp[i] = dp[i-1] + dp[i-2]
TC & SC: O(n)
"""

# Approach 1: Brute Force
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         return self.climb(0, n)
#     def climb(self, step, n):
#         if step == n:
#             return 1
#         if step > n:
#             return 0
#         return self.climb(step+1, n) + self.climb(step+2, n)

# Apprach 2: Memoization
# brute force requires to build the whole tree and returns the number of leaf in the tree
# using the fact that repeated path occurs while building the tree, memoize each values that is already calculated
# this will build the tree from the top to bottom (when n, 1 is added, and these are accumulated to 0)
# TC: O(n), SC: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        return self.climb(0, n, memo)
    def climb(self, step, n, memo):
        if step > n:
            return 0
        if step == n:
            return 1
        if memo[step]:
            return memo[step]
        memo[step] = self.climb(step+1, n, memo) + self.climb(step+2, n, memo)
        return memo[step]

# Approach 3: DP
# Bottom up
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0]*(n+1)
#         dp[0] = 1
#         dp[1] = 1
        
#         for i in range (2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]