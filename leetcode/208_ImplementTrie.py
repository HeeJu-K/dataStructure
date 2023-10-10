"""
Appraoch: Trie
Tip: do not need to implement dfs as return type is bool
"""
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.child = [None]*26
        self.is_end = False
        self.count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def _charToIdx(self, ch) -> int:
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            charIntVal = self._charToIdx(char)
            if node.child[charIntVal] is None:
                new_node = TrieNode(char)
                node.child[charIntVal] = new_node
                node = new_node
            else:
                node = node.child[charIntVal]
        node.is_end = True
        node.count += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            charIntVal = self._charToIdx(char)
            if node.child[charIntVal] is None:
                return False
            node = node.child[charIntVal]
        return True if node.is_end else False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        self.output = []
        for char in prefix:
            charIntVal = self._charToIdx(char)
            if node.child[charIntVal] is None:
                return False
            else: 
                node = node.child[charIntVal]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)