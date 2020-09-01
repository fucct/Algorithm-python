class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        isMinus = 1
        result = 0
        idx = 0
        if not s:
            return 0
        if s[idx] == '-':
            isMinus = -1
            idx += 1
        elif s[idx] == '+':
            isMinus = 1
            idx += 1
        while idx < len(s) and s[idx].isnumeric():
            result *= 10
            result += int(s[idx])
            idx += 1

        result *= isMinus
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -2 ** 31:
            return -2 ** 31
        return result
