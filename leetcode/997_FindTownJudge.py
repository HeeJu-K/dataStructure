"""
find a node that is not going out 
first approach: dict
iterate through the arrays, note down the nodes that has no outgoing relationship
if every node is connected to a specific node, return
second approach:
store down being trusted and trusting sums, return the person with n-1 and 0
third approach:
use a single array to store down the trusted sum
"""
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_sum = [0]*(n+1)
        #edge case
        if n == 1 and len(trust) == 0: return 1
        # print(trust_sum)
        for [a, b] in trust:
            trusted_sum[a] -= 1
            trusted_sum[b] += 1
        # print("after adding", trust_sum, trusted_sum)
        for i in range (n+1):
            if trusted_sum[i] == n-1:
                return i
        return -1
