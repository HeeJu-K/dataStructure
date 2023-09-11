"""
dict, set() -> both O(1) to see if exists
Approach 1: set()  O(nlogn)
since its longest of the sequence -> only one `max_len` variable to store and update
find the start of the sequence and go to the last
Approach 2: set() Optimized O(n) -> only visit each elements once
Expand from any element in the sequence, delete the elements
"""

"""
Approach: dict, set() -> both O(1) to see if exists
since its longest of the sequence -> only one `max_len` variable to store and update
find the start of the sequence and go to the last
"""
### Approach 1, O(nlogn)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         max_len = 0
#         for num in nums:
#             if num-1 not in nums_set:
#                 length = 1
#                 while num+length in nums_set:
#                     length += 1
#                 max_len = max(max_len, length)

#         return max_len
### Approach 2, O(n)
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