class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        highest = 0
        l = len(heights)
        for i in range (l-1, -1, -1):
            if heights[i]>highest:
                res.append(i)
                highest = heights[i]

        return res[::-1]