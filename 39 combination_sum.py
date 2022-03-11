from copy import copy

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []

    def dfs(i, cur, targ):
        if targ == target:
            res.append(copy(cur))
            return

        if targ > target or i >= len(candidates):
            return

        cur.append(candidates[i])
        dfs(i, cur, targ + candidates[i])

        cur.pop()
        dfs(i + 1, cur, targ)

    dfs(0, [], 0)
    return res
