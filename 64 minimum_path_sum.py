class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row = [0] * (n - 1) + [grid[m - 1][n - 1]]
        for j in range(n - 2, -1, -1):
            row[j] = row[j+1] + grid[m - 1][j]

        last_col = [0] * (m - 1) + [grid[m - 1][n - 1]]
        for i in range(m - 2, -1, -1):
            last_col[i] = last_col[i + 1] + grid[i][n - 1]

        for i in range(m - 2, -1, -1):
            new_row = [0] * (n - 1) + [last_col[i]]
            for j in range(n - 2, -1, -1):
                new_row[j] = min(new_row[j + 1], row[j]) + grid[i][j]
            row = new_row
        return row[0]


grid = [[1,3,1],[1,5,1],[4,2,1]]
a = Solution().minPathSum(grid)
