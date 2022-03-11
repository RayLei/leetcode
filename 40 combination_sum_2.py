def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []

    def dfs(pos, cur, total):
        if total == target:
            res.append(cur.copy())
            return

        if total > target:
            return

        prev_val = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev_val:
                continue
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            prev_val = candidates[i]
            cur.pop()

    dfs(0, [], 0)
    return res



nums = [10,1,2,7,6,1,5]
target = 8
