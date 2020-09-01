class Solution7:
    def reverse(self, x: int) -> int:
        result = 0
        results = []
        isMinus = False
        if x == 0:
            return 0
        if x < 0:
            isMinus = True
        x = abs(x)
        while x != 0:
            num = x % 10
            results.append(num)
            x //= 10

        for num in results:
            result *= 10
            if result == 0 and num == 0:
                continue
            result += num
        if result > 2 ** 31:
            return 0

        if isMinus:
            return -result
        return result
