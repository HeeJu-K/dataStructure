class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        l, r = 1, num/2
        while l<=r:
            mid = (l+r)//2
            if num < mid**2:
                r = mid - 1
            elif mid**2 < num:
                l = mid + 1
            else:
                return True
        return False