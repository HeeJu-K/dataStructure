class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] # stores char and index

        for index, item in enumerate(s):
            # print("stack in for:", stack)
            if item == "(":
                stack.append((item, index))
            elif item == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((item, index))
        
        while len(stack):
            _, index = stack.pop()
            # print("here", s[:index],"here", s[index+1:])
            s = s[:index]+ s[index+1:]
        return s