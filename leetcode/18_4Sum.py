class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, quad = [], []
        nums.sort()

        def kSum(k, start, target_sum):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    # do not consider duplicates, as sum will be the same
                    # due to the ascending order and is considering next two elements of the list, with a sum of four, this will not skip the sum made from identical elements
                    if i>start and nums[i] == nums[i-1]: 
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target_sum - nums[i])
                    quad.pop()
                return
            l, r = start, len(nums)-1
            while l<r:
                if nums[l]+nums[r] < target_sum:
                    l+=1
                elif nums[l]+nums[r] > target_sum:
                    r-=1
                else:
                    result.append(quad + [nums[l], nums[r]])
                    l+=1 # can either be l or r
                    while l<r and nums[l] == nums[l-1]: #to prevent infinite loop
                        l+=1
        kSum(4, 0, target)
        return result
