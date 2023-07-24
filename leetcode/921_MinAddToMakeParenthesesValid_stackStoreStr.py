class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # store instance not addition in stack, pop closed ones, add closing ones that doesn't have starting parentheses
        stack = []
        num_close = 0
        for elem in s:
            if elem == "(":
                stack.append(elem)
            else:
                if stack:
                    stack.pop()
                else:
                    num_close += 1
        return len(stack) + num_close