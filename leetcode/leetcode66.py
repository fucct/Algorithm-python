from typing import List


class Solution66:
    def plusOne(self, digits: List[int]) -> List[int]:
        adder = 0
        for idx in range(1, len(digits) + 1):
            index = idx * -1
            if idx == 1:
                addNum = digits[index] + 1 + adder
            else:
                addNum = digits[index] + adder
            if addNum >= 10:
                addNum -= 10
                adder = 1
            else:
                adder = 0
            digits[index] = addNum
        if adder == 1:
            return [1, *digits]
        return digits
