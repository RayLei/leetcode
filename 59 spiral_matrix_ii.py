class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        min_row, max_row = 0, n - 1
        min_col, max_col = 0, n - 1
        dict_res = {}

        i, j = 0, -1
        cur = 0

        def convert_dict_to_list(dict_res):
            res = []
            for i in range(n):
                tmp = []
                for j in range(n):
                    tmp.append(dict_res[i, j])
                res.append(tmp)
            return res




        while cur < n ** 2:
            if (i, j) == (min_row, min_col-1):
                while j < max_col:
                    j += 1
                    cur += 1
                    dict_res[i, j] = cur
                if cur == n**2:
                    return convert_dict_to_list(dict_res)

            if (i, j) == (min_row, max_col):
                while i < max_row:
                    i += 1
                    cur += 1
                    dict_res[i, j] = cur
                if cur == n**2:
                    return convert_dict_to_list(dict_res)

            if (i, j) == (max_row, max_col):
                while j > min_col:
                    j -= 1
                    cur += 1
                    dict_res[i, j] = cur
                if cur == n**2:
                    return convert_dict_to_list(dict_res)

            if (i, j) == (max_row, min_col):
                while i > min_row + 1:
                    i -= 1
                    cur += 1
                    dict_res[i, j] = cur
                if cur == n**2:
                    return convert_dict_to_list(dict_res)

            min_row, max_row = min_row + 1, max_row - 1
            min_col, max_col = min_col + 1, max_col - 1

        return convert_dict_to_list(dict_res)


n = 3
print(Solution().generateMatrix(n))

