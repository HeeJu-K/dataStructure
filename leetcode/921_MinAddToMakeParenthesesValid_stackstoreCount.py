class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        prev = 0
        stack = []
        result = 0
        for char in s:
            if not stack and char == ")":
                result += 1
            elif char == "(" and prev == 0:
                stack.append(1)
            elif char == "(" and prev == "(":
                stack.append(stack.pop()+1)
            elif char == "(" and prev == ")":
                stack.append(1)
            elif char == ")" and stack:
                tmp = stack.pop()-1
                if tmp!=0:
                    stack.append(tmp)
            elif char == ")" and not stack:
                result+=1
            prev = char
        for elem in stack:
            result += abs(elem)
        return result