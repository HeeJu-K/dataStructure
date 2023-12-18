class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # DFS
        def dfs(tmp, visited):
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    dfs(tmp+[nums[i]], visited)
                    visited.remove(nums[i])
        visited = set()
        res = []
        dfs([], visited)
        return res
