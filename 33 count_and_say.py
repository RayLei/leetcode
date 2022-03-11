def backtrack(n):
    if n == 1:
        return "1"

    prev_res = backtrack(n - 1)
    res = ''
    for i, v in enumerate(prev_res):
        if i == 0:
            cnt = 0
            prev = v

        if v == prev:
            cnt += 1
        else:
            res += '{}{}'.format(cnt, prev)
            cnt = 0
            prev = v

        if i == len(prev_res) - 1:
            res += '{}{}'.format(cnt, v)
    return res


result = backtrack(2)
print(result)
