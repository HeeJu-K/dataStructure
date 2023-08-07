from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_time = 1440
        def timeTo0000(timePoint:str) -> int:
            # hour = int(timePoint[0:2])
            # minute = int(timePoint[3:6])
            hour, minute = timePoint.split(":")
            minutes_passed = int(hour)*60 + int(minute)
            
            return minutes_passed

        timePoints.sort()
        print(timePoints)
        for i in range(len(timePoints)-1):
            diff = abs(timeTo0000(timePoints[i+1]) - timeTo0000(timePoints[i]))
            if diff>720: 
                diff = 1440-diff
            min_time = min(min_time, diff)
        first_diff = abs(timeTo0000(timePoints[len(timePoints)-1]) - timeTo0000(timePoints[0]))
        if first_diff>720: 
            first_diff = 1440-first_diff
        min_time = min(min_time, first_diff)
        return min_time
    
if __name__ ==  "__main__":
    solution = Solution()
    
    # res = solution.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    #                      word="ABCCED")
    res = solution.findMinDifference(
        # timePoints=["12:12","00:13"]
        timePoints=["01:01","02:01"]
    )
    print(res)