"""
dict, set() -> both O(1) to see if exists

Approach 1: set()  O(nlogn)
since its longest of the sequence -> only one `max_len` variable to store and update
find the start of the sequence and go to the last
Approach 2: set() Optimized O(n) -> only visit each elements once
Expand from any element in the sequence, delete the elements
Approach 3: UF -> O(n)

"""
### Approach 1&2
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         max_len = 0
#         while nums_set:
#             low = high = nums_set.pop()
#             while low-1 in nums_set or high+1 in nums_set:
#                 if low-1 in nums_set:
#                     nums_set.remove(low-1)
#                     low -= 1
#                 if high+1 in nums_set:
#                     nums_set.remove(high+1)
#                     high += 1
#             max_len = max(max_len, high-low+1)
#         return max_len

### Approach 3 UF
class UF:
    def __init__(self, n):
        self.parent = [i for i in range (n)]
        self.length = [1]*n
    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])
    def union(self, u, v):
        uu = self.find(u)
        vv = self.find(v)
        if uu != vv:
            if self.length[uu]>self.length[vv]:
                self.parent[vv] = uu
                self.length[uu] += self.length[vv]
            else:
                self.parent[uu] = vv
                self.length[vv] += self.length[uu]
                
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nodes = {}
        uf = UF(n)
        for i, num in enumerate(nums):
            if num in nodes:
                continue # skip duplicate numbers 
            nodes[num] = i

            if num-1 in nodes:
                uf.union(i, nodes[num-1])
            if num+1 in nodes:
                uf.union(i, nodes[num+1])
        return max(uf.length)
        
            