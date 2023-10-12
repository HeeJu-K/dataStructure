"""
Approach: sort nlogn
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        d = [key for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True)]
        return d[:k]