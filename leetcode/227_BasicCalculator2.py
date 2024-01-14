class Solution:
    def calculate(self, s):
        s += "+"
        sign = "+"
        numStack = []
        tmp = 0
        for c in s:
            if c == " ": continue
            elif c.isdigit():
                tmp = tmp*10 + int(c)
            else: 
                if sign == "+": numStack.append(tmp)
                elif sign == "-": numStack.append(tmp*-1)
                elif sign == "*":
                    prevNum = numStack.pop()
                    numStack.append(prevNum * tmp)
                elif sign == "/": 
                    prevNum = numStack.pop()
                    numStack.append(int(prevNum / tmp))
                tmp = 0
                sign = c
        return sum(numStack)