# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Use DFS + Recursion
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    def dfs(self, node, targetSum ):
        if not node:
            return 0
        # 计算从当前节点开始的路径和
        numPaths = 0
        if node.val == targetSum:
            numPaths += 1
        # 继续递归计算左子树和右子树的路径和
        numPaths += self.dfs(node.left, targetSum - node.val)
        numPaths += self.dfs(node.right, targetSum - node.val)
        return numPaths