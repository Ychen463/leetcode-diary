# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: BFS
# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         queue = deque([root])
#         result = []

#         while queue:
#             level = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             result.append(level[-1])
#         return result

# # Method 1: BFS: Two Queues
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        if root is None:
            return []
        rightside = []
        nextLevel = deque([root])

        while nextLevel:
            currLevel = nextLevel
            nextLevel = deque()

            while currLevel:
                node = currLevel.popleft()
                if node.left: # First one must be Left Child
                    nextLevel.append(node.left)
                if node.right: # Second one must be Left Child
                    nextLevel.append(node.right)
                # So the last would be the last right child
            rightside.append(node.val)
        return rightside
            
