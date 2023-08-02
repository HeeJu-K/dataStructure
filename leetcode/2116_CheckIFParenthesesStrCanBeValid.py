"""
Approach: two way validation to avoid cases such as __((
    It has to return False but will return True as there is no checking of sequences
    Making it two way will make it ))__, where False will be returned right away when ) is met
"""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:  
        def valid(s, locked, op):
            lock = unlo = 0
            n = len(s)
            for i in range (n):
                if locked[i] == "1" and s[i] == op:
                    lock+=1
                elif locked[i] == "1" and s[i] != op:
                    if lock > 0: lock -= 1
                    elif unlo>0: unlo-=1
                    else: return False
                else: 
                    unlo += 1
                if lock<0: 
                    return False
            if (unlo-lock)%2==0 and unlo>=lock : return True
            else: return False
        return valid(s, locked, "(") and valid(s[::-1], locked[::-1], ")")
