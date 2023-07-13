# ### Optimized brute Force, DP, O(n^2)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReach = [False]*n
        i = 0
        canReach[0] = True
        for i in range(n):
            if canReach[i] :
                for j in range (nums[i], 0, -1):
                    if i+j < n:
                        canReach[i+j] = True
                    if i+j == n-1:
                        return True
        return canReach[n-1]