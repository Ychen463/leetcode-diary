# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# -------- Method 1: DFS + Recursion
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currSum):
            nonlocal count
            if node is None:
                return
            currSum += node.val
            count += prefixSums[currSum - targetSum]
            prefixSums[currSum] +=1
            dfs(node.left, currSum)
            dfs(node.right, currSum)

            prefixSums[currSum] -= 1

        count = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        dfs(root, 0)
        return count




        # def dfs(node: Optional[TreeNode], curr_sum: int) -> None:
        #     nonlocal count
        #     if not node:
        #         return        
        #     # 更新当前前缀和
        #     curr_sum += node.val  
        #     # 检查当前前缀和减去目标值是否存在于哈希表中
        #     count += prefix_sums[curr_sum - targetSum]
        #     # 更新哈希表中当前前缀和的计数
        #     prefix_sums[curr_sum] += 1
            
        #     dfs(node.left, curr_sum)# 递归处理左子树
        #     dfs(node.right, curr_sum)# 递归处理右子树

        #     # 递归结束后，恢复哈希表中当前前缀和的计数
        #     prefix_sums[curr_sum] -= 1
        
        # count = 0 # 用于记录满足条件的路径数量。
        # prefix_sums = defaultdict(int) # 用于记录前缀和及其出现的次数。
        # prefix_sums[0] = 1  # 初始化前缀和为0的情况
        
        # dfs(root, 0)
        # return count

        