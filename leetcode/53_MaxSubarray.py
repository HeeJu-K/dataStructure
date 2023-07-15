class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # when the array is all negative, we return the single smallest element value
        # in other cases, use maxSum and curSum to maintain the maximum sum

        maxSum = float("-inf")
        curSum = 0

        for i in range (len(nums)):
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum
