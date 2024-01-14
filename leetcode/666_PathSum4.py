class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = self.right = None

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # translate the arrays into position: value hashmap
        treeMap = {num//10: num%10 for num in nums}


        def dfs(node, curSum):
            nonlocal res
            depth, pos = node//10, node%10
            curSum += treeMap[node]
            left = (depth+1) *10 + pos*2 - 1
            right = (depth+1) *10 + pos*2
            if left in treeMap:
                dfs(left, curSum)
            if right in treeMap:
                dfs(right, curSum)
            if left not in treeMap and right not in treeMap:
                res += curSum

        res = 0
        root = nums[0]//10
        dfs(root, 0)

        return res