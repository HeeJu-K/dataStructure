class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        # find one, delete one, change to another -> repeat
        # add ith to tmp, divide as left and right, continue
        l = len(nums)
        res = []
        def backtrack(nums, tmp):
            if not len(nums):
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrack(nums, [])
        return res