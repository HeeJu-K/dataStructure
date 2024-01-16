class TrieNode:
    def __init__(self):
        self.isFile = False
        self.child = collections.defaultdict(TrieNode)
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
    
    def findPath(self, node, path):
        path = path.split('/')[1:]
        for p in path:
            node = node.child[p]
        return node

    def ls(self, path: str) -> List[str]:
        if path == '/':
            # return self.root.child as node only contains instance not the child as well, as no files were actually created
            return sorted(self.root.child.keys())

        node = self.findPath(self.root, path)
        if node.isFile:
            return [path.split('/')[-1]]
        else: 
            return sorted(node.child.keys())

    def mkdir(self, path: str) -> None:
        node = self.findPath(self.root, path)
        return 

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.findPath(self.root, filePath)
        node.content += content
        node.isFile = True
        return

    def readContentFromFile(self, filePath: str) -> str:
        node = self.findPath(self.root, filePath)
        return node.content 


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)