class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        res = ""
        stack = []
        for d in dirs:
            if d == "" or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/'+'/'.join(stack)