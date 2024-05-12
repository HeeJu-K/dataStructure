"""
Binary Search, Sort
O(nlogn)
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse = True)
        for idx in range (len(citations)):
            if citations[idx] >= idx+1:
                h = max(h, idx+1)
        return h