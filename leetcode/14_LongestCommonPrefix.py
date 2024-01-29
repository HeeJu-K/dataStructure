"""
Binary Search
M number of words, smallest length of N
time complexity: MlogN
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        minlen = len(min(strs, key=lambda x: len(x)))
        l, r = 0, minlen-1
        equal = False
        while l<=r:
            mid = (l+r)//2 
            for i in range(len(strs)-1):
                if strs[i][l:mid+1] == strs[i+1][l:mid+1]:
                    equal = True
                else:
                    equal = False
                    break
            if equal:
                l = mid + 1
            else:
                r = mid - 1


        return strs[0][:l]

