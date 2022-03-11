class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        min_row, max_row = 0, len(matrix) - 1
        min_col, max_col = 0, len(matrix[0]) - 1

        i, j = 0, -1
        cnt = 0
        res = []
        total = len(matrix) * len(matrix[0])

        while cnt < total:
            if (i, j) == (min_row, min_col - 1):  # top left corner
                while j < max_col:
                    j += 1
                    res.append(matrix[i][j])
                if len(res) == total:
                    break

            if (i, j) == (min_row, max_col):  # top right corner
                while i < max_row:
                    i += 1
                    res.append(matrix[i][j])
                if len(res) == total:
                    break

            if (i, j) == (max_row, max_col):  # bottom right corner
                while j > min_col:
                    j -= 1
                    res.append(matrix[i][j])
                if len(res) == total:
                    break

            if (i, j) == (max_row, min_col):  # bottom left corner
                while i > min_row + 1:
                    i -= 1
                    res.append(matrix[i][j])
                if len(res) == total:
                    break

            cnt = len(res)
            min_row, max_row = min_row + 1, max_row - 1
            min_col, max_col = min_col + 1, max_col - 1
        return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))
