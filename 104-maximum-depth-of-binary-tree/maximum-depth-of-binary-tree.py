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
        st = []
        if root is not None:
            st.append((1, root))
        depth = 0
        while st:
            current_depth, root = st.pop()
            if root is not None:
                depth = max(depth, current_depth)
                st.append((current_depth+1, root.left))
                st.append((current_depth+1, root.right))
        return depth

