# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    def dfs(self, node, maxValue):
        if node is None:
            return 0
        goods = 1 if node.val >= maxValue else 0
        maxValue = max(node.val,maxValue)
        goods += self.dfs(node.left,maxValue)
        goods += self.dfs(node.right,maxValue)
        return goods


        