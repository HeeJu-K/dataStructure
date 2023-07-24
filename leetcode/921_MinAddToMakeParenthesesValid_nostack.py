class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_open = num_close = 0
        for elem in s:
            if elem == "(":
                num_open += 1
            else:
                if num_open:
                    num_open -= 1
                else: 
                    num_close += 1
        return num_open + num_close
        