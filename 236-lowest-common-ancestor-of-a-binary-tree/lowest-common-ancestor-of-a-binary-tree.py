# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_ancestors(node, target, path):
            if not node:
                return False
            path.append(node)
            if node == target:
                return True
            if find_ancestors(node.left, target, path) or find_ancestors(node.right, target, path):
                return True
            path.pop()
            return False
        p_ancestors = []
        q_ancestors = []

        find_ancestors(root, p, p_ancestors)
        find_ancestors(root, q, q_ancestors)

        lca = None
        for u,v in zip(p_ancestors,q_ancestors):
            if u == v:
                lca= u
            else:
                break

        return lca
