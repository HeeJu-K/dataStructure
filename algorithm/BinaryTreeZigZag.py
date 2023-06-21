# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        output = []
        #overall idea is to use dfs, search through each leaves make spaces for each level. 
        # after this, add left and right nodes consecutively, using level to change directions
        def dfs( node, level, output):
            
            if node == None:
                return  #when reached end
            if len(output) <= level: #make positions for each level
                output += [[]] # []+[[]]=[[]], [[]]+[[]]=[[],[]]
            
            #iterate to the leftmost then right
            dfs(node.left, level+1, output)
            dfs(node.right, level+1, output)

            #store each data according to level, use append for left -> right and insert at front for right -> left
            if level%2 == 0:
                output[level].append(node.val)
            else:
                output[level].insert(0, node.val) #insert(i, ele) is a O(n) operation, inserts ele in the ith index
                
        #call the dfs function of root node
        dfs(root, 0, output)
        return output
