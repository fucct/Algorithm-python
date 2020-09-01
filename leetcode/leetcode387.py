import collections


class Solution387:
    def firstUniqChar(self, s: str) -> int:
        table = dict(collections.Counter(s))

        minIdx = len(s)
        for key in list(table.keys()):
            if table.get(key) == 1:
                minIdx = min(minIdx, s.index(key))

        if minIdx == len(s):
            return -1
        return minIdx
