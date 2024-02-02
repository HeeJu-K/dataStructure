class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
    
        def helper(length):
            seen = set()
            for i in range (len(s) - length):
                substring = s[i:i+length+1]
                if substring in seen:
                    return True
                seen.add(substring)
            return False

        l, r = 0, len(s)-1
        while l<r:
            mid = (l+r)//2
            
            if helper(mid):
                l = mid+1
            else:
                r = mid
        return l