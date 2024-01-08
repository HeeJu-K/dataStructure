class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        h1 = h2 = 0
        m, n = len(word), len(abbr)
        cnt = 0
        while h1 < m and h2 < n:
            if abbr[h2].isdigit():
                if cnt == 0 and abbr[h2] == "0": return False
                cnt = cnt*10 + int(abbr[h2])
                h2 += 1
                
            else:
                h1 += cnt 
                cnt = 0
                if h1<m and h2<n and word[h1] != abbr[h2]:
                    return False
                
                h1 += 1
                h2 += 1
        if not (h1+cnt == m and h2 == n): return False
        return True
