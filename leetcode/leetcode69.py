class Solution69:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        return self.binarySearch(0, x, x)

    def binarySearch(self, start: int, end: int, x: int) -> int:
        middle = (start + end) // 2
        if middle ** 2 <= x < (middle + 1) ** 2:
            return middle
        elif middle ** 2 > x:
            return self.binarySearch(start, middle, x)
        else:
            return self.binarySearch(middle, end, x)
