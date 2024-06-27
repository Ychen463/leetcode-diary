class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hm = {}
        for i in range(len(edges)):
            hm[edges[i][0]] = hm.get(edges[i][0],0)+1
            hm[edges[i][1]] = hm.get(edges[i][1],0)+1
            if hm[edges[i][0]] == len(edges):
                return edges[i][0]
            if hm[edges[i][1]] == len(edges):
                return edges[i][1]

        