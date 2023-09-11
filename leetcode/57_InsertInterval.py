"""
Approach 1: Insert than merge
Approach 2: Append to result array
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: return [newInterval]
        # if n == 1: 
        #     if  
        #         return [[min(newInterval[0], intervals[0][0]), max(newInterval[1], intervals[0][1])]]
            
        if newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
        else:
            for i in range (n):
                if intervals[i][0]<=newInterval[0] and (i+1 < n and newInterval[0]<intervals[i+1][0]) or (i+1 >= n):
                    intervals.insert(i+1, newInterval)
                    break
        # print("intervals: ", intervals)

        # [[1, 2], [3, 5], [4, 8], [6, 7], [8, 10], [12, 16]]

        i = 0
        while i < len(intervals)-1:
            # print("intervals start merge", intervals, i)
            if intervals[i][1]>=intervals[i+1][0] :
                # print("intervals in if ", intervals[i][1], intervals[i+1][1], i)
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
                # print("intervals if end", intervals, i)
            else: i += 1
                
        return intervals
