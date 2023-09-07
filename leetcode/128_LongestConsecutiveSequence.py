"""
dict, set() -> both O(1) to see if exists
Approach 1: set()  O(nlogn)
since its longest of the sequence -> only one `max_len` variable to store and update
find the start of the sequence and go to the last
Approach 2: set() Optimized O(n) -> only visit each elements once
Expand from any element in the sequence, delete the elements
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        while nums_set:
            low = high = nums_set.pop()
            while low-1 in nums_set or high+1 in nums_set:
                if low-1 in nums_set:
                    nums_set.remove(low-1)
                    low -= 1
                if high+1 in nums_set:
                    nums_set.remove(high+1)
                    high += 1
            max_len = max(max_len, high-low+1)
        return max_len