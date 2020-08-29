from typing import List


class Solution14:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 0:
            return ""

        if size == 1:
            return strs[0]

        strs.sort()

        first = (char for char in strs[0])
        last = (char for char in strs[-1])
        result = []

        for a in list(zip(first, last)):
            pair = set(a)
            if len(pair) == 1:
                result.append(tuple(pair)[0])
            else:
                break
        return ''.join(result)
