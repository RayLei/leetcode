class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            top, btm = l, r
            for i in range(r-l):
                top_left = matrix[top][l + i]

                # rotate bottom left to top left
                matrix[top][l + i] = matrix[btm - i][l]

                # rotate bottom right to bottom left
                matrix[btm - i][l] = matrix[btm][r - i]

                # rotate top right to bottom right
                matrix[btm][r - i] = matrix[top + i][r]

                # rotate top left to top right
                matrix[top + i][r] = top_left

            l, r = l + 1, r - 1

