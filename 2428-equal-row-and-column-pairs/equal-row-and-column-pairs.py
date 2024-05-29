class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # rows, columns = len(grid), len(grid[0])
        # hashmap_row = {}
        # hashmap_col = {}
        # for i in range(rows):
        #     row_tuple = tuple(grid[i])
        #     hashmap_row[row_tuple] = hashmap_row.get(row_tuple, 0) + 1
        # for j in range(columns):
        #     col_tuple = tuple(grid[i][j] for i in range(rows))
        #     hashmap_col[col_tuple] = hashmap_col.get(col_tuple, 0) + 1

        # counter = 0
        # for rk, rv in hashmap_row.items():
        #     if rk in hashmap_col.keys():
        #         counter += rv * hashmap_col.get(rk)
        # return counter
        
        # # Method 2, optimal
        # rows, columns = len(grid), len(grid[0])
        # counter = 0
        # hashmap_row = {}
        # for i in range(rows):
        #     row_tuple = tuple(grid[i])
        #     hashmap_row[row_tuple] = hashmap_row.get(row_tuple, 0) + 1

        # for j in range(columns):
        #     col_tuple = tuple(grid[i][j] for i in range(rows))
        #     counter += hashmap_row.get(col_tuple,0)
        # return counter

        # Method 3 Prefix-Trie
        count = 0
        trie = Trie()

        for row in grid:
            trie.insert(row)
        for j in range(len(grid)):
            each_col = [grid[i][j] for i in range(len(grid))]
            count += trie.search(each_col)
        return count
class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
class Trie:
    def __init__(self):
        self.trie = TrieNode()
    def insert(self, array):
        root = self.trie
        for a in array:
            if a not in root.children:
                root.children[a] = TrieNode()
            root = root.children[a]
        root.count +=1
    def search(self, array):
        root = self.trie
        for a in array:
            if a in root.children:
                root = root.children[a]
            else:
                return 0
        return root.count
        
        