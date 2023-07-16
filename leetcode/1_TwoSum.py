class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ### to search if key exists in dictionary, it takes O(1)
        numsMap = {}
        # for i in range(n):
        #     numsMap[nums[i]] = i
        
        for i in range (n):
            findNum = target - nums[i]
            if findNum in numsMap.keys():
                return [i, numsMap[findNum]]
            numsMap[nums[i]] = i