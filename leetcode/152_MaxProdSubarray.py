"""
Approach: Kadane's Algorithm (DP)
-> O(n)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currentMax = currentMin = maxProd = nums[0]
        for i in range (1, n):
            tmp = max(nums[i], nums[i]*currentMax, nums[i]*currentMin)
            currentMin = min(nums[i], nums[i]*currentMax, nums[i]*currentMin)
            currentMax = tmp
            maxProd = max(currentMax, maxProd)
            # print(nums[i], currentMax, currentMin, maxProd)
        return maxProd