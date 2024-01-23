class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        l = len(part)
        while i <= len(s)-l:
            if s[i:i+l] == part:
                s = s[:i]+s[i+l:]
                i -= l
            i += 1
        return s