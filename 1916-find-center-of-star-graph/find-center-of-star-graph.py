# # ============= Approach 1: Degree Count =============
# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         hm = {}
#         for i in range(len(edges)):
#             hm[edges[i][0]] = hm.get(edges[i][0],0)+1
#             hm[edges[i][1]] = hm.get(edges[i][1],0)+1
#             if hm[edges[i][0]] == len(edges):
#                 return edges[i][0]
#             if hm[edges[i][1]] == len(edges):
#                 return edges[i][1]
#         return -1

# ============= Approach 2: Greedy =============
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 由于输入总是一个星形图，因此中心节点出现在每条边上。
        # 为了找到这个中心节点，我们只需在前两条边中找到那个共同出现的节点即可。
        # 原因是，在星形图中，只有中心节点的度大于1。
        first_edge, second_edge = edges[0], edges[1]
        if first_edge[0] in second_edge:
            return first_edge[0]
        else:
            return first_edge[1]
        return -1


