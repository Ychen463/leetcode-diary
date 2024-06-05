# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # Method 1: BFS
# from collections import deque
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return []
#         queue = deque([root])
#         res_dict = defaultdict(int)
#         level_num = 0
#         while queue:
#             level = []
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             level_num += 1
#             res_dict[level_num] = sum(level)
        
#         return max(res_dict, key =lambda x: res_dict[x])      

# =======
# # Method 2: DFS
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        res_dict = defaultdict(int)
        
        def helper( node, level):
            if not node:
                return
            res_dict[level] += node.val
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root,0)
        print(res_dict)
        return max(res_dict, key = lambda x: res_dict[x]) +1
