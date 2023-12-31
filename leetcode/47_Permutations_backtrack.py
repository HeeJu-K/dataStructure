class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # backtrack 
        nums.sort()
        def backtrack(nums, path, prev):
            
            if not len(nums):
                res.append(path)
                return
            for i in range (len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i]+nums[i+1:], path+[nums[i]], nums[i])
        res = []
        backtrack(nums, [], None)
        return res