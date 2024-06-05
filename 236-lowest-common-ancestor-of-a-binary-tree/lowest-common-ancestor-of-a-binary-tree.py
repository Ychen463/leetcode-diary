# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1, 2 lists
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def find_ancestors(node, target, path):
#             if not node:
#                 return False
#             path.append(node)
#             if node == target:
#                 return True
#             if find_ancestors(node.left, target, path) or find_ancestors(node.right, target, path):
#                 return True
#             path.pop()
#             return False
#         p_ancestors = []
#         q_ancestors = []

#         find_ancestors(root, p, p_ancestors)
#         find_ancestors(root, q, q_ancestors)

#         lca = None
#         for u,v in zip(p_ancestors,q_ancestors):
#             if u == v:
#                 lca= u
#             else:
#                 break

#         return lca
# ==================================================================
# Method 2: Recursive Approach
# class Solution:
#     def __init__(self):
#         # Variable to store LCA node.
#         self.ans = None
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def recurse_tree(currentNode: TreeNode) -> bool:
#             if not currentNode:
#                 return False
#             left = recurse_tree(currentNode.left)
#             right = recurse_tree(currentNode.right)

#             mid = currentNode == p or currentNode == q
#             if int(mid) + int(left) + int(right) >=2:
#                 self.ans = currentNode
#             return mid or left or right
#         recurse_tree(root)
#         return self.ans

# ==================================================================
# Method 3: Iterative using parent pointers
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root:None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node # 记录parent
                stack.append(node.left)
            if node.right:
                parent[node.right] = node # 记录parent
                stack.append(node.right)
         # 存储 p 的所有祖先
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = parent[p]

        # 找到 q 的第一个公共祖先
        while q not in p_ancestors:
            q = parent[q]

        return q