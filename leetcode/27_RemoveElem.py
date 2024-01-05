class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        k = 0
        while l+k<len(nums):
            if nums[l] == val:
                while l!=r and nums[r] == val:
                    r -= 1
                    k += 1
                nums[l] = nums[r]
                r -= 1
                k += 1
            l += 1
        
        return len(nums) - k