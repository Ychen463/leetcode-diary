# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)
    def getLeaves(self, root):
        leaves = []
        self.dfs(leaves,root)
        return leaves
    def dfs(self, leaves, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaves.append(node.val)
        self.dfs(leaves,node.left)
        self.dfs(leaves,node.right)
