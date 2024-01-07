class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid

        return -1
        