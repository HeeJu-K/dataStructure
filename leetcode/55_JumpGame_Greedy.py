### Greedy Algorithm

### move goal to the front one by one if the i-1 can be reached
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         goal = len(nums)-1

#         for i in range (len(nums)-2, -1, -1):
#             if i+nums[i]>= goal:
#                 goal = i

#         return True if goal==0 else False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        pos = l-1
        for i in range (l-1, -1, -1):
            if i+nums[i] >= pos:
                pos = i
        return pos == 0