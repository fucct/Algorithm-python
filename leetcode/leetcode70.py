class Solution70:
    def climbStairs(self, n: int) -> int:
        result = [1, 2]
        if n <= 2:
            return result[n - 1]
        else:
            for idx in range(2, n):
                result.append(result[idx - 1] + result[idx - 2])
            return result[n - 1]
