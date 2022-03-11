class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        row = [1] * n
        for j in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][j] == 1:
                row[:j + 1] = [0] * (j + 1)

        last_col = [1] * m
        for i in range(m - 1, -1, -1):
            if obstacleGrid[i][n-1] == 1:
                last_col[:i + 1] = [0] * (i + 1)

        for i in range(m - 2, -1, -1):
            newRow = [1] * n
            newRow[n-1] = last_col[i]
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j] if obstacleGrid[i][j] != 1 else 0
            row = newRow
        return row[0]


grid = [[0],[0]]
test = Solution()
a = test.uniquePathsWithObstacles(grid)
