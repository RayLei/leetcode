# def updateTimes(signalOne, signalTwo):
#     # Write your code here
#     maxSig = -1
#     res = 0
#     for i in range(min(len(signalOne), len(signalTwo))):
#         if signalOne[i] == signalTwo[i] and signalOne[i] > maxSig:
#             maxSig = signalOne[i]
#             res += 1
#     return res
#
#
# signalOne = [1, 2, 3, 4, 5]
# signalTwo = [5, 4, 3, 2, 1]
#
# a=updateTimes(signalOne, signalTwo)
# print(a)


# def maxPerksItems(cartridges, dollars, recycleReward, perksCost):
#     # Write your code here
#     l, r = 0, cartridges
#     prv_l = -1
#     while l <= r and prv_l != l:
#         mid = (l + r) // 2
#         if mid * perksCost > dollars + (cartridges - mid) * recycleReward:
#             r = mid
#         elif mid * perksCost < dollars + (cartridges - mid) * recycleReward:
#             prv_l = l
#             l = mid
#         else:
#             return mid
#
#     return l
#
# a=maxPerksItems(4, 8, 3, 4)
# print(a)


def getSubstringCount(s):
    # Write your code here
    l = r = 0
    res = 0
    cnt = {}

    while r < len(s):
        cnt[s[r]] = 1 + cnt.get(s[r], 0)

        if r == len(s)-1 and cnt.get('0', 0) != cnt.get('1', 0):
            cnt[s[l]] -= 1
            l += 1
            r = l
            cnt = {}
        elif max(cnt.values()) > 0 and cnt.get('0', 0) == cnt.get('1', 0):
            res += 1
            l += 1
            r = l
            cnt = {}
        else:
            r += 1
    return res


s = '001100011'
print(getSubstringCount(s))
