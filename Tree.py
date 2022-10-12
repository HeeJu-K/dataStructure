# ----- Tree -----

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child): # in here the input parameter is a node
        child.parent = self # 
        self.children.append(child) # self will be the parent of the newly made child node
    
    def get_level(self):
        level = 0
        itr = self.parent
        while itr:
            itr = itr.parent
            level = level+1
        return level

    def print_tree(self):
        spaces = '-'* self.get_level()*3
        print('|'+spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode("lenses")

    canon = TreeNode("canon")
    root.add_child(canon)

    sony = TreeNode("sony")
    root.add_child(sony)
    sony.add_child(TreeNode("70-200"))

    fuji = TreeNode("fuji")
    root.add_child(fuji)
    fuji.add_child(TreeNode("16-55"))
    fuji.add_child(TreeNode("55-250"))

    nikon = TreeNode("nikon")
    root.add_child(nikon)
    nikon.add_child(TreeNode("14-24"))

    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
