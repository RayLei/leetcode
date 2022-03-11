class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # find which row
        first_col = [row[0] for row in matrix] + [matrix[-1][-1] + 1]
        l, r = 0, m

        while r - l >= 2:
            mid = (l + r) // 2
            if target == first_col[mid]:
                return True
            elif target > first_col[mid]:
                l = mid
            else:
                r = mid
        row = matrix[l]

        # binary search
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if target == row[mid]:
                return True
            elif target > row[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
a = Solution().searchMatrix(matrix, target)
print(a)
