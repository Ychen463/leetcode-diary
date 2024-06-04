# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # Method 1: DFS + Recursion
    # def goodNodes(self, root: TreeNode) -> int:
    #     return self.dfs(root, root.val)
    # def dfs(self, node, maxValue):
    #     if node is None:
    #         return 0
    #     goods = 1 if node.val >= maxValue else 0
    #     maxValue = max(node.val,maxValue)
    #     goods += self.dfs(node.left,maxValue)
    #     goods += self.dfs(node.right,maxValue)
    #     return goods
    # ========================================
    # Method 2: iterative + DFS
    # def goodNodes(self, root: TreeNode) -> int:
    #     st = [(root, float("-inf"))]
    #     goodNums = 0
    #     while st:
    #         node, maxValue = st.pop()
    #         if maxValue <= node.val:
    #             goodNums += 1
    #         if node == None:
    #             return currentGoodNums
    #         if node.left:
    #             st.append((node.left, max(maxValue, node.val)))
    #         if node.right:
    #             st.append((node.right, max(maxValue, node.val)))
    #     return goodNums

    # ========================================
    # Method 2: BFS
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, float('-inf'))])
        goods = 0
        while queue:
            node, max_so_far = queue.popleft()
            if node.val >= max_so_far:
                goods += 1
            maxValue = max(node.val, max_so_far)
            if node.left:
                queue.append((node.left, maxValue))
            if node.right:
                queue.append((node.right, maxValue))
        return goods
