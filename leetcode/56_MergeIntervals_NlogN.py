"""
Approach: NlogN
Sort it at first, add merged intervals to `result` to return
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        result = []

        # sort with first index, choose .sort to reduce space memory
        # intervals = sorted(intervals, key=lambda x:x[0])
        intervals.sort(key=lambda x:x[0])

        prev = intervals[0]
        for interval in intervals[1:]:
            if prev[1]>=interval[0]:
                prev[1] = max(interval[1], prev[1])
            else:
                result.append(prev)
                prev = interval
        result.append(prev)
        return result
