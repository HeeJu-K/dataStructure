class RandomizedSet:

    def __init__(self):
        self.hm = {} # key: element value, val: element index in list
        self.list = []        

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        else: 
            self.hm[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.hm:
            idx = self.hm[val]
            last_elem = self.list[-1]
            self.list[idx] = last_elem
            self.hm[last_elem] = idx
            self.list.pop()
            del self.hm[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()