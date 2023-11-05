"""
no duplicates -> sort OR hashset
Approach 1: sort + two pointer
Approach 2: sort + one pass hashset
Approach 3: no sort + two hashsets
"""

### Approach 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            if nums[i]<=0:
                if i == 0 or nums[i-1] != nums[i]:
                    self.twoPointer(i, nums, res)
        return res

    def twoPointer(self, i, nums, res):
        l = len(nums)
        left, right = i + 1, l - 1 
        while left < right:
            if nums[left] + nums[right] + nums[i] < 0:
                left += 1
            elif nums[left] + nums[right] + nums[i] > 0:
                right -= 1
            else: 
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
