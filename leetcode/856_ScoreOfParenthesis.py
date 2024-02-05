class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        for char in s:
            tmp = 0
            if char == "(":
                stack.append(char)
            else:
                prev = stack.pop()
                if prev == "(":
                    stack.append(1)
                else: # when prev is int
                    if stack[-1] is not "(":
                        while stack[-1] is not "(":
                            tmp += prev
                            prev = stack.pop()
                        if stack[-1] == "(":
                            stack.pop()
                            stack.append((tmp+prev)*2)
                        else:
                            stack.append(tmp+prev)
                    else:
                        stack.pop()
                        stack.append(2*prev)
                        
        return sum(stack)
                    









        # stack = []
        # res = 0
        # count = 0

        # for p in s:
        #     if p == "(":
        #         stack.append(0)
        #     else:
        #         cur = stack.pop()
        #         if cur == 0:
        #             count = 1
        #         else:
        #             count = 2 * cur
        #         if not stack:
        #             res += count
        #         else:
        #             stack[-1] += count
        
        # return res



        # stack = [0]
        # for c in s:
        #     if c == '(':
        #         stack.append(0)
        #     else:
        #         if stack[-1] == 0:
        #             stack.pop()
        #             stack[-1] += 1
        #         else:
        #             tmp = 2 * stack.pop()   
        #             stack[-1] += tmp

        # return stack[0]