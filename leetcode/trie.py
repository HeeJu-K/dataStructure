class TrieNode:
	# a node in the trie structure
	def __init__(self, char):
		self.char = char
		# self.children = {}
		self.children = [None]*26
		self.is_end = False
		self.counter = 0 # (if this node's is_end is True)

class Trie:
	
	# Trie data structure class
	def __init__(self):
		self.root = TrieNode("") # initialize an empty node

	# use only 'a' through 'z' and lower case
	def _charToIndex(self,ch):
		return ord(ch)-ord('a')

	def insert(self, word):
		
		node = self.root
		for char in word:
			charIntValue = self._charToIndex(char)
			if node.children[charIntValue] is None:
				# for the case where character is not found
				new_node = TrieNode(char)
				node.children[charIntValue] = new_node
				node = new_node
			else:
				# for the case where character is found
				node = node.children[charIntValue]
		
		node.is_end = True # mark end of word
		node.counter += 1 # update node frequency

	def dfs(self, node, prefix):
		"""
		Args:
			- node: node to start with
			- prefix: the current prefix
		"""
		if node.is_end:
			self.output.append((prefix + node.char, node.counter))

		for child in node.children:
			if child is not None:
				self.dfs(child, prefix + node.char)

	def query(self, prefix):
		"""
			Retrieve all words stored in the trie with the prefix
			sort the words by the number of times they've been inserted
		"""
		self.output = []
		node = self.root

		for char in prefix:
			charIntValue = self._charToIndex(char)
			if node.children[charIntValue] is None:
				return []
			else:
				node = node.children[charIntValue]
		self.dfs(node, prefix[:-1])

		return sorted(self.output, key=lambda x:x[1], reverse=True)
		
if __name__ == "__main__":
	trie = Trie()
	trie.insert("abc")
	trie.insert("abcd")
	trie.insert("abf")
	trie.insert("abcfe")
	print(trie.query("abc"))