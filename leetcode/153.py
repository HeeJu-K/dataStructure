class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        cur = nums[0]
        l_lim = 0
        r_lim = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        while l_lim <= r_lim:
            print("l_lim ", l_lim, " r_lim ", r_lim)
            mid = (l_lim + r_lim)//2
            print("mid ", mid, " nums[mid] ", nums[mid])
            if nums[mid] < cur:
                res = nums[mid]
                cur = nums[mid]
                print("res: ", res)
                r_lim = mid-1
            elif nums[mid] > cur:
                l_lim = mid+1
            else:
                return cur
                
        return res


#solve in O(logn) time, min() is O(N)
# 4 5 6 7 0 1 2 3

# 0 1 2 3 4 5 6 
# 6 0 1 2 3 4 5 
# 4 5 6 0 1 2 3
# 2 3 4 5 6 0 1