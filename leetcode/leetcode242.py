import collections


class Solution242:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = collections.Counter(s)
        counter2 = collections.Counter(t)
        return counter1 == counter2
