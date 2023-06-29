# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        ### append [] in a [] gives [[], []] structure
        queue = deque()
        ### deque structure allows append and popleft
        queue.append(root)
        # print(queue, len(queue))
        while queue:
            level = []
            for i in range(len(queue)): # all neighbors in the same level added
                node = queue.popleft()
                # print("node: ", node)
                #check is node is null
                if node:
                    #add current level to level, children to queue
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res
        