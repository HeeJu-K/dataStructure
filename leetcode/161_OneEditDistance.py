# class Solution:
#     """
#     @param s: a string
#     @param t: a string
#     @return: true if they are both one edit distance apart or false
#     """
#     def is_one_edit_distance(self, s: str, t: str) -> bool:
#         # write your code here
#         i = j = 0
#         flag = 0
#         while i<len(s):
#             if j<len(t) and s[i]!=t[j]:
#                 if flag: return False
#                 flag = 1
#                 if i+1<len(s) and s[i+1] == t[j]: i+=1
#                 elif j+1<len(t) and s[i] == t[j+1]: j+=1
#             i+=1
#             j+=1

#         if abs(len(s) - len(t)) == 1 and not flag:
#             return True
#         if flag == 1: return True
#         else: return False


### can be solved with two pointers
class Solution:

    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        # write your code here
        n = len(s)
        m = len(t)
        l = min(n, m)
        if abs(n - m)>2: return False
        for i in range (l):
            if s[i]!=t[i]:
                if n == m:
                    return s[i+1:] == t[i+1:] 
                else:
                    return s[i+1:] == t[i:] or s[i:] == t[i+1:]
        if n!=m: return s[:l] == t[:l]
        return False