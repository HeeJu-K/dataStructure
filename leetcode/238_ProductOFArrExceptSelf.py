"""
edge cases: zeros. when there are multiple zeros the number on that index can be either 0 or non zero value
Approach: 
During the loop, have left side multiplications and right side multiplications
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        pre, post = 1, 1

        for i in range (n):
            res[i] *= pre
            pre *= nums[i]
            res[n-i-1] *= post
            post *= nums[n-i-1]        
       
        return res