class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        cur = 0
        lists = []
        for i in range (n):
            if seats[i]:
                if not len(lists) :
                    lists.append(cur)
                else:
                    lists.append(ceil(cur/2))
                cur = 0
            else:
                cur += 1
        lists.append(cur)

        return max(lists)