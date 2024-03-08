class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        l = len(nums)
        i = 1
        for j in range (1, l):
            if nums[j-1] == nums[j]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[i] = nums[j]
                i += 1
                
        return i