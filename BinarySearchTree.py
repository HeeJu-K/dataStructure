# ----- Binary Search Tree -----



##set in python removes repeated items

## Search complexity: each itr search space reduced to half -> O(log n)
### search efficiency depends highly on the balance of left and right sides of the tree

## Complexity:
### Unsorted Array:
#### - Search: O(n) -> compare through the whole array
#### - Insert: O(1) -> insert at the end
#### - Remove: O(n) -> remove an element and copy items in the back to front (worst case shift n-1 elements)
### Linked List:
#### - Search: O(n) -> compare through the whole array
#### - Insert: O(1) -> insert at the head
#### - Remove: O(n) -> worst case search through whole array to find item to delete
### Sorted Array:
#### - Search: O(log n) -> binary search halves items to search every time
#### - Insert: O(n) -> worst case have to move every elements 
#### - Remove: O(n) -> worst case have to move every elements 
### Binary Search Tree:
#### - Search: O(log n) -> binary search halves items to search every time (do 2^k steps to find the last element, n/2^k = 1, k = log2 n)
#### - Insert: O(log n) -> cost same as search
#### - Remove: O(log n) -> cost same as search

## Depth First Search: in order traversal, pre-order traversal, post-order traversal (named by root node position)
### in order traversal: visit left subtree -> root -> right subtree 
### pre-order traversal: visit root node -> left subtree -> right subtree
### post-order traversal: visit left subtree -> right subtree -> root

## Breadth First Search


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):

        #when data already exists in the tree
        if data == self.data: 
            return

        #add to left subtree
        if data < self.data:

            if self.left: # if is not leaf, recursively visit its left child to add node
                self.left.addChild(data)
            else : #if leaf, make a new node and add to left side
                self.left = BinarySearchTree(data) 
        
        #add to left subtree
        else: 
            if self.right: # if is not leaf, recursively visit its right child to add node
                self.right.addChild(data)
            else : #if leaf, make a new node and add to right side
                self.right = BinarySearchTree(data) 
    
    def in_order_traversal(self):

        itr = []

        if self.left:
            itr += self.left.in_order_traversal()
        
        itr.append(self.data)

        if self.right:
            itr += self.right.in_order_traversal()

        return itr
    
    def find_min(self):
        if self.left == None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right == None:
            return self.data
        return self.right.find_max()

    def search(self, value):

        if value == self.data:
            return True
        if value < self.data:
            if self.left: 
                return self.left.search(value) # have to put return here so that value is passed to main function, else True is only passed and left here
            else: 
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    # deletion in BST. delete node with two child: copy minimum from the right subtree or copy maximum from the left subtree
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val) #connecting the subtree of deleted node to the node
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else: # when current node is the value you wish to delete
            if self.left == None and self.right == None: #couldn't find the value to delete in the tree, return none
                return None
            if self.left == None:
                return self.right # if no left subtree, return right subtree to replace with current node
            if self.right == None:
                return self.left
            min_val = self.right.find_min() # find the min value of right subtree
            self.data = min_val # replace current node data with min value from right subtree
            self.right = self.right.delete(min_val) # this will return the deleted right subtree, which will be set as the new right subtree
            #for using max value in left subtree to replace the current node
            # max_val = self.left.find_max() # find the min value of right subtree
            # self.data = max_val # replace current node data with min value from right subtree
            # self.left = self.left.delete(max_val)
        return self

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0 # should use this to make it work in recursion
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):

    rootNode = BinarySearchTree(elements[0])

    for i in range (1, len(elements)):
        rootNode.addChild(elements[i])
    
    return rootNode

if __name__ == '__main__':
    nums = [7, 1, 3, 9, 2, 2, 0]
    tree = build_tree(nums)
    print(tree.in_order_traversal())
    print(tree.search(4))
    print(tree.find_min())
    print(tree.find_max())
    tree.delete(2)
    print(tree.in_order_traversal())
    print(tree.calculate_sum())