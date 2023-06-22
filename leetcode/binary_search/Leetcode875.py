class Solution:
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #lower and upper boundary of binary search  
        l, r = 1, max(piles)
        #worst case eating one pile each time
        res = r 

        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            # if eating faster or equal (meaning condition is satisfied)
            # slower the eating speed, update result as might be solution
            if hours <= h: 
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        return res
