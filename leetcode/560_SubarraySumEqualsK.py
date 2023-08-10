"""
Approach: O(n) | Prefix Sum + dict | "contiguous sequence" 
# Consider edge case where [0,0,0,0], index 0,1,2,3,01,12,23,012,123,0123 all has to be counted
Storing up prefix sum with index as keys will only add 1 if prefix exists
-> Thus store the frequency of prefix sum
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1} # base case for cursum == k
        n = len(nums)
        cursum = 0
        cnt = 0
        for i in range (n):
            cursum += nums[i]
            if cursum-k in d : # looking for keys
                cnt += d[cursum-k] # add the frequency
            if cursum in d:
                d[cursum] += 1
            else: d[cursum] = 1
        return cnt