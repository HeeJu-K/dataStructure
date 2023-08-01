"""
Approach 1:
Time Complexity:O(n*k) Space Complexity:O(n*k) 
where n is number of elements and k is largest value
positive integers. An array that stores w[i] of the value and randomly pick one from it

Approach 2:
Time Complexity: init -> O(n) pickIndex -> O(logn) Space Complexity:O(n)
store sums of weights
1 3 4
1 4 8
get random integer within the total sum and find closest, either through bisect method O(logn) or binary search O(logn)
BISECT: bisect_left(list, val) returns the index val can be added to in a sorted list
"""
class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.sums = []
        self.total = 0
        for i in range (self.n):
            self.total += w[i]
            self.sums.append(self.total)
        # print(self.sums, self.total)
    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        l, r = 0, self.n-1
        while l<=r:
            mid = (l+r)//2
            if rand<self.sums[mid]:
                r = mid-1
            elif self.sums[mid]<rand:
                l = mid+1
            else: return mid
        return l
        # return bisect_left(self.sums, rand)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()