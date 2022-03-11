import numpy as np

def platesBetweenCandles(s, queries):
    """
    :type s: str
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    res = []
    last_, next_, presum_ = [], [], []
    left_anchor, right_anchor, cnt = np.nan, np.nan, 0

    for i, x in enumerate(s):
        if x == '|':
            left_anchor = i
        else:
            cnt += 1
        last_.append(left_anchor)
        presum_.append(cnt)

    for j, y in enumerate(s[::-1]):
        if y == '|':
            right_anchor = len(s) - 1 - j
        next_.append(right_anchor)
    next_ = next_[::-1]

    for q in queries:
        l, r = next_[q[0]], last_[q[1]]
        tmp = presum_[r] - presum_[l] if r >= l else 0
        res.append(tmp)
    return res


s="***|**|*****|**||**|*"
queries=[[4,5],[14,17],[5,11],[15,16]]
platesBetweenCandles(s, queries)
