"""
Approach: BackTracking
Time Complexity: O(C(n,k))
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def getcomb(start, comb):
            if len(comb) == k:
                # print("if ", res)
                res.append(comb[:])
            else:
                for i in range (start, n+1):
                    comb.append(i)
                    # print("else ", i, start, comb)
                    getcomb(i+1, comb)
                    comb.pop()
        
        getcomb(1, [])
        return res