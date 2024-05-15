class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        l = len(s)
        for i in range (l//2):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        
        res = ''

        for c in s:
            if c != '':
                res += c + ' '

        return res[:len(res)-1]