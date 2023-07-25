"""
dp approach:
i2 = i3 = i5 = 0
find min, append or update list to maintain smallest 
   2  3  5
1  2  3  5

2  4  6  10
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        ans = [0]*n
        ans[0] = 1
        for i in range(1,n):
            ans[i] = min(ans[i2]*2, ans[i3]*3, ans[i5]*5)
            if ans[i] == ans[i2]*2:
                i2 += 1
            if ans[i] == ans[i3]*3:
                i3 += 1
            if ans[i] == ans[i5]*5:
                i5 += 1
        return ans[n-1]