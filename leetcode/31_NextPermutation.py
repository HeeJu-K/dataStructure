"""
Approach: Two Pointer
Find first decreasing element from right, 
swap with element just larger than that element on its right side, (rest are decreasing)
reverse the elements on right to make it increasing

Time Complexity: O(n)
Space Complexity: O(n), can be optimized to O(1) by implementing swap in for loop then function
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # edge case, if one element return directly
        if len(nums) <= 1:
            return
        
        i = len(nums) - 1
        while nums[i - 1] >= nums[i] and i > 1:
            i -= 1
        j = i - 1
        if nums[0] >= nums[1] and j == 0:
            nums = self.swap(nums, 0, len(nums)-1)
            return
            
        # find the first smaller item 
        while i<len(nums)-1 and nums[i+1] > nums[j] :
            i += 1
        # j is found

        nums[i], nums[j] = nums[j], nums[i] 

        # reverse the rest, from i (included)
        nums = self.swap(nums, j + 1, len(nums)-1)
    def swap (self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr