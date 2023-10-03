"""
Approach 1: 
sort by ending index, remove the longer one
when overlaps, do not have to update the prev, current interval will be updated anyways, prev will only have same or less ending time than current interval
Appraoch 2:
sort by starting index, remove the longer one
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cnt = 0
        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] > interval[0]: # overlaps
                cnt += 1
            else: # does not overlap
                prev = interval
        return cnt