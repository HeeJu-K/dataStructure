"""
KMP
l = 3
0 1 2 3 4 5 6 7 8 9 10 11
d a a b c b a a b c b  c
i = 4
a b c
j = 2

0123456789
eemckxmckx
emckx
01234
emckx
i = 0
j = 0
finding i after deleting
start searching from l-1 previous of current starting substring search
new_i + l = i - l + 1
"""
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        j = 0
        l = len(part)
        while 0 <= i < len(s) and j < l:
            if s[i] == part[j]:
                if j == l-1:
                    s = s[:i-l+1]+s[i+1:]
                    i = max(i - 2*l + 1, 0)
                    j = 0
                else:
                    i += 1
                    j += 1
            else: 
                i = i - j + 1
                j = 0
                
        return s