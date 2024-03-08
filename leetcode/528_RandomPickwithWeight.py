"""
for w 2 2 3 5
prefix sum 
2 4 7 12
1 2 | 3 4 | 5 6 7 | 8 9 10 11 12 |
rand < number in index -> search space becomes l ~ mid, mid included
rand > number in index -> search space becomes mid+1 ~ r
for ex if rand is 8, index 0, 1, 2 for prefix array is not included.
"""

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.w_sum = prefix_sum

    def pickIndex(self) -> int:
        rand = random.random()*self.w_sum
        l, r = 0, len(self.prefix_sums)-1
        while l<r:
            mid = (l+r)//2
            
            if self.prefix_sums[mid] < rand:
                l = mid + 1 
            else:
                r = mid
        return l
        
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()