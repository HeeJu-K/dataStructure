class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        def backtrack(cur, cand):
            res.append(cur)
            if len(cur) == l:
                return
            for i in range (len(cand)):
                backtrack(cur+[cand[i]], cand[i+1:])
            
        backtrack([], nums)
        return res