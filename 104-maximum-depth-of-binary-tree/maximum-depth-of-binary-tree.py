# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Method 1: Recursion
        # if root == None:
        #     return 0
        # else:
        #     leftMaxDepth = self.maxDepth(root.left)
        #     rightMaxDepth = self.maxDepth(root.right)
        #     return max(leftMaxDepth,rightMaxDepth) +1

        # ------------------------
        # # Method 2: Iteration with Stack
        # st = []
        # if root is not None:
        #     st.append((1, root))
        # depth = 0
        # while st:
        #     current_depth, root = st.pop()
        #     if root is not None:
        #         depth = max(depth, current_depth)
        #         st.append((current_depth+1, root.left))
        #         st.append((current_depth+1, root.right))
        # return depth

        # Method 3: DFS and Tail Recursion
        if not root:
            return 0
        self.next_items = []
        self.max_depth = 0
        self.next_items.append((root, 0))
        return self.next_maxDepth()
    def __init__(self):
        self.next_items = []
        self.max_depth = 0
    def next_maxDepth(self):
        if not self.next_items:
            return self.max_depth
        next_node, next_level = self.next_items.pop(0)
        next_level +=1
        self.max_depth = max(next_level, self.max_depth)
        if next_node.left:
            self.next_items.append((next_node.left, next_level))
        if next_node.right:
            self.next_items.append((next_node.right, next_level))
        return self.next_maxDepth()
    
