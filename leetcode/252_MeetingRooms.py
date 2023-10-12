"""
Approach 1: arr, count O(N+M)
rooms array to mark start and end as 1, -1, running sum of the rooms > 1, return False
Approach 2: heapify O(n)

"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        heapq.heapify(intervals)
        max_end = 0
        
        while intervals:
            start, end = heapq.heappop(intervals)
            if start<max_end:
                return False
            max_end = max(max_end, end)
        return True