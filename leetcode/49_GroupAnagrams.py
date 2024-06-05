"""
Approach:
Sort each of the strings and use as keys
TC: iteration: N, sort of each strings: KlogK when K is length of longest string -> O(NKlogK)
SC: data stored in hashmap: O(NK)
---
improve:
Mark characters used in each string, make a hashmap which keys are array length of 26
TC: O(NK)
SC: O(NK)
"""
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # first approach
#         hm = defaultdict(list)
#         for s in strs:
#             hm[''.join(sorted(s))].append(s)
#             # alternatively can do:
#             # hm[tuple(sorted(s))].append(s)
#             # hashmap keys can take tuples or strings
#         return hm.values()

# improved ver:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        # hm: DefaultDict[int, List[str]] = collections.defaultdict(list)
        for s in strs:
            alphabets = [0]*26
            for c in s:
                alphabets[ord(c) - ord('a')] += 1
            hm[tuple(alphabets)].append(s)
        return hm.values()