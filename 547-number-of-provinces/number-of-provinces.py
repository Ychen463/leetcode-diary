# ========= DFS ========
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            for neighbor, is_connected in enumerate(isConnected[node]):
                if neighbor not in visited and is_connected:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count +=1
        return count


        