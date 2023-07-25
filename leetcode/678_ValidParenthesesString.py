class Solution:
    def checkValidString(self, s: str) -> bool:
        openS = []
        starS = []
        for index, elem in enumerate(s):
            if elem == "(":
                openS.append(index)
            elif elem == "*":
                starS.append(index)
            else:
                if openS: openS.pop()
                elif starS: starS.pop()
                else: return False
        while openS:
            # cur = openS.pop()
            if starS and openS.pop() < starS.pop():
                continue
            else: return False
        return True