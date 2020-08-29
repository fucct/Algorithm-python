class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0:
            if len(needle) == 0:
                return 0
            return -1
        for idx in range(len(haystack)):
            if idx + len(needle) > len(haystack):
                return -1
            if haystack[idx:idx + len(needle)] == needle:
                return idx
        return -1
