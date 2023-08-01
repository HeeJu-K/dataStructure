"""
Approach: DP
Time Complexity:O(m*n) Space Complexity:O(m*n)
Sum of all characters - same characters
Construct a 2d array where rows are chars in s1 and cols are chars in s2
if s1[i] == s2[j], store s1[i-1]s2[j]+s1[i]s2[j-1]+cur ASCII

Further Optimization:
Space Complexity: O(min(m,n))
Since we only need the previous row, 2d array can be reduced to 1d
"""
"""
Note: when copying list, use [:]
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        totalsum = 0
        [s1, s2] = [s1, s2] if len(s1)>=len(s2) else [s2, s1]
        m = len(s1)
        n = len(s2)
        prev = tmp = [0]*n
        
        for i in range(m):
            totalsum+=ord(s1[i])
            tmp = prev[:]
            for j in range(n):
                if not i: totalsum+=ord(s2[j])
                if s1[i] == s2[j]:
                    if not j: 
                        prev[j] = ord(s1[i])
                    else:
                        prev[j] = ord(s1[i]) + tmp[j-1]
                else:
                    if not j: 
                        # print("first col", j, tmp, prev)
                        prev[j] = tmp[j]
                    else:
                        prev[j] = max(prev[j-1],tmp[j])
                # print(s1[i], s2[j], totalsum, prev, j, prev[j-1], tmp)
        
        return totalsum - 2*prev[n-1]
        