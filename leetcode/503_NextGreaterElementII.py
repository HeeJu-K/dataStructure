class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = [] #stores stack_ind
        
        for n in range(2):
            for i in range (len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]
                stack.append(i)

        return result