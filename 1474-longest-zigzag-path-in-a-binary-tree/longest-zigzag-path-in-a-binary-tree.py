# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longestPath = 0
        def dfs(prevDirection, node, currPath): 
            # prevDirection = True: goLeft
            # prevDirection = False: goRight
            nonlocal longestPath
            if not node:
                return
            longestPath = max(longestPath, currPath)
            if prevDirection: # if go left
                dfs(False, node.left, currPath+1)
                dfs(True, node.right, 1)
            else: # if go right
                dfs(True, node.right, currPath+1)
                dfs(False, node.left, 1)

        dfs(True, root, 0)  # Start by going left from root

        return longestPath
        
        