class Solution58:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        arr = s.rstrip().split(" ")
        return len(arr[-1])
