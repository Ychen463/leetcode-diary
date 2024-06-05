# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: BFS： One Queue + Level Size Measurements
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

# ======================================================
# # Method 1: BFS: Two Queues
# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
#         if root is None:
#             return []
#         rightside = []
#         nextLevel = deque([root])

#         while nextLevel:
#             currLevel = nextLevel
#             nextLevel = deque()

#             while currLevel:
#                 node = currLevel.popleft()
#                 if node.left: # First one must be Left Child
#                     nextLevel.append(node.left)
#                 if node.right: # Second one must be Left Child
#                     nextLevel.append(node.right)
#                 # So the last would be the last right child
#             rightside.append(node.val)
#         return rightside
            
# ======================================================
# # Method 2: BFS: One Queue + Sentinel
# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
#         if root is None:
#             return []
#         rightside = []
#         queue = deque([root,None])
#         curr = root
#         while queue:
#             prev, curr = curr, queue.popleft()
#             while curr: # add child nodes in the queue
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#                 prev, curr = curr, queue.popleft()
#             rightside.append(prev.val)
#             if queue:
#                 # 之所以要None是因为 prev, 
#                 # curr 最后需要curr是null但是prev是最后一个node，这样可以保持queue 非空
#                 queue.append(None) 
#         return rightside

# ======================================================
# Method 4: DFS
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 
        if root is None:
            return []
        rightside = []
        def helper( node, level):
            if len(rightside) == level:
                rightside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    helper(child, level+1)
        helper(root,0)
        return rightside