class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        hashmap_row = {}
        hashmap_col = {}
        counter = 0
        for i in range(rows):
            row_tuple = tuple(grid[i])
            hashmap_row[row_tuple] = hashmap_row.get(row_tuple, 0) + 1
            # i = 0, j = 0,1,2
        for j in range(columns):
            col_tuple = tuple(grid[i][j] for i in range(rows))
            hashmap_col[col_tuple] = hashmap_col.get(col_tuple, 0) + 1
        print('hashmap_row',hashmap_row)
        print('hashmap_col',hashmap_col)
        counter = 0
        for rk, rv in hashmap_row.items():
            if rk in hashmap_col.keys():
                counter += rv * hashmap_col.get(rk)
        print(counter)
        return counter
