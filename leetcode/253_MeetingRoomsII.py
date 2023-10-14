class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        d = collections.defaultdict(int)

        for start, end in intervals:
            d[start] += 1
            d[end] -= 1
        
        d = sorted(d.items())
        
        prev = res = 0
        for time, cnt in d:
            prev += cnt
            res = max(res, prev)
        return res