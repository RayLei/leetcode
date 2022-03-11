class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1:
        #     return 1
        # if n == 1:
        #     return 1
        #
        # res = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        #
        # return res

        row = [1] * n
        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + row[j]
            row = new_row

        return row[0]

m, n = 3, 2
test = Solution()
a = test.uniquePaths(m, n)
print(a)
