# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # = key
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # if node 左右都有node，在中间
                largerMinNode = self.findMinNode(root.right)
                root.val = largerMinNode.val
                root.right = self.deleteNode(root.right,largerMinNode.val)
        return root
    def findMinNode(self, node):
            while node.left:
                node = node.left
            return node

