"""
Approach:
Sliding Window
a dict to store occured char and it's latest indices
left and right pointer to indicate the current window
when char in dictionary, check if index is in window or not. 
-> yes: reduce window size ->> use max to compare cur longest and longest after reducing
-> no: increase window size
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxdis = dis = 0
        l = r = 0

        # lastest = float(-inf)
        for r in range(len(s)):
            if s[r] not in seen.keys(): 
                maxdis = max(r-l+1, maxdis)
            else: 
                if seen[s[r]]<l: # no need to adjust sliding window
                    maxdis = max(r-l+1, maxdis)
                else: #adjust sliding window
                    l = seen[s[r]]+1
            seen[s[r]] = r
            
        return maxdis