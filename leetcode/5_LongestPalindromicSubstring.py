class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        l = len(s)
        print(s, l)
        dp = [0] * (l) # will store the radiuses on each char
        r = c = 0

        max_c = max_i = 0

        for i in range(1, l):
            mirror = c - ( i - c )
            if i < r:
                # c - i - r
                # mirror ensures the center to left side of the element,
                # r-i ensures right side of the element
                # take the smaller between the two
                dp[i] = max(0, min(dp[mirror], r-i))
            while i+1+dp[i]<l and s[i-1-dp[i]] == s[i+1+dp[i]]:
                dp[i] += 1
            max_i = i if dp[i]>max_c else max_i
            max_c = max(dp[i], max_c)
            if i+dp[i] > r:
                r = i+dp[i]
                c = i
        s = s[max_i-max_c:max_i+max_c] if max_i%2 == 1 else s[max_i-max_c:max_i+max_c+1]
        return s.replace("#", "")