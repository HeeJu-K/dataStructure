"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

### the adjList[0] is the neighbors of the first node, adjList[1] the second, and so on

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        q = deque([node])
        ### hashmap to store cloned nodes
        # start with the first node
        cloned = {node.val: Node(node.val, [])} 
        
        while q:
            cur_node = q.popleft() # cur_node is a node with .val and .neighbors

            # iterate neighbors, each neighbors have .val 
            for neighbor in cur_node.neighbors:
                # bfs add node in result hashmap if not visited
                if neighbor.val not in cloned:
                    cloned[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                # when node is added in result clone, add neighbors value
                cloned[cur_node.val].neighbors.append(cloned[neighbor.val])
        return cloned[node.val]