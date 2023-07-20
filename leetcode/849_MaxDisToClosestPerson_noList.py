class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        cur = 0
        max_dis = 1
        for i in range (n):
            if seats[i]:
                if i == cur :
                    max_dis = max(cur, max_dis)
                else:
                    max_dis = max(max_dis, ceil(cur/2))
                cur = 0
            else:
                cur += 1
        max_dis = max(cur, max_dis)
        return max_dis