from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1:
            return [strs]

        prev_res = self.groupAnagrams(strs[:-1])
        last_w = strs[-1]

        for elem in prev_res:
            contain = Counter(elem[0]) == Counter(last_w)

            if contain:
                elem.append(last_w)
                break

        if not contain:
            prev_res.append([last_w])

        return prev_res


