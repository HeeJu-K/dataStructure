"""
Approach 1: sort, see if duplicate exists 
    - python sort -> O(nlogn)
    - 
Approach 2: dictionary -> O(n) 
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            if num in dup.keys(): return True
            else: 
                dup[num] = 1
        return False