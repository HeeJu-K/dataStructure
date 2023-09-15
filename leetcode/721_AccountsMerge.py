"""
Approach: Union Find, Hash Map
"""
class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)] # account the email beloongs to
        self.rank = [1]*n
    def find(self, x):
        if self.parent[x] == x:
            return x
        else: 
            return self.find(self.parent[x])
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            else:
                self.parent[p1] = p2
                if self.rank[p1] == self.rank[p2]:
                    self.rank[p2] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UF(n)
        emailToAcc = defaultdict(list)
        for i, account in enumerate(accounts):
            for acc in account[1:]: # 0-index is name
                if acc in emailToAcc: 
                    uf.union(emailToAcc[acc], i) # link the names when there are same addresses
                else:
                    emailToAcc[acc] = i
        # by here, email addresses are linked to indices
        # now we want to join the emails with same indices
        emailGroup = defaultdict(list)
        for email, i in emailToAcc.items():
            par = uf.find(i)
            emailGroup[par].append(email)
        res = []
        for i, emails in emailGroup.items(): # here the i's are indexed from each accounts
            name = accounts[i][0]
            res.append([name]+sorted(emailGroup[i]))
        return res