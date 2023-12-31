class Solution:
    def maximumLength(self, s: str) -> int:
        special_cnt = defaultdict(list)
        l = len(s)
        cur_len = 1
        res = -1
        for i in range (l):
            if i<l-1 and s[i] == s[i+1] :
                cur_len += 1
            else: 
                special_cnt[s[i]].append(cur_len)
                cur_len = 1
        for v in special_cnt.values():
            v.sort(reverse = True)
            v = v[:3]
            if len(v) >= 3:
                max_v = max(v[0]-2, v[1], v[2]) if v[0]-1 == v[1] else max(v[0]-2, v[1]-1, v[2])
            elif len(v) == 2 and v[1] >= v[0]-1:
                max_v = v[0] - 1
            else:
                max_v = v[0]-2
            if max_v > 0:
                res = max(max_v, res)
        return res