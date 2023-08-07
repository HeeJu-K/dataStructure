from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ### this method uses backtracking, which uses a dfs approach to explore all possible solutions by incrementally building a candidate solution and backtracking when necessary.
        ### in here, cur is a stack to easily add and pop the candidates when needed and invalid

        res = []

        def dfs(i, cur, sum)->List:
            print("dfs: ", i, cur, sum, res)
            #found the result
            if sum == target:
                ### must use cur.copy(), or else the modifying cur will be added to res, resulting res to change everytime cur is changed
                res.append(cur.copy())
                print("result appended, candidate: ", candidates[i], res)
                return
            #out of index or solution path invalid, backtrack
            if i>=len(candidates) or sum>target:
                return

            cur.append(candidates[i])
            #keeps on adding the same candidate
            dfs(i, cur, sum+candidates[i])
            #backtrack to previous path, previous addition of candidate was not valid
            cur.pop()
            #try out the next candidate, previous invalid candidate not added
            dfs(i+1, cur, sum)
        
        dfs(0, [], 0)
        return res

if __name__ ==  "__main__":
    solution = Solution()
    res = solution.combinationSum(candidates=[2,3,6,7], target=7)
    print(res)
