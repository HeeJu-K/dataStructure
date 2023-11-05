class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.DFS(n, res, "", 0, 0)
        return res
    def DFS(self, n, res, s, left, right):
        if left < n:
            self.DFS(n, res, s+"(", left+1, right)
        if right < left:
            self.DFS(n, res, s+")", left, right+1)
        if len(s) == 2*n:
            res.append(s)