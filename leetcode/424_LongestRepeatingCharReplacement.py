"""
Approach: Sliding Window, dict
maxCount + k = longest
Maintain count dict to keep track of frequency of each char in current window
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxlen = 0
        count = {}
        res = 0
        length = len(s)
        for r in range(length):
            if s[r] not in count:  
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            maxlen = max(maxlen, count[s[r]])
            if maxlen + k < r-l+1:
                count[s[l]] -= 1
                l += 1
            else:
                res = max(r-l+1, res)
        return res 