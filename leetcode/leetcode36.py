from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            col = []
            if not self.isNotDuplicated(board[i]):
                return False
            for j in range(len(board)):
                col.append(board[j][i])
            if not self.isNotDuplicated(col):
                return False
        for i in range(0, 3):
            for j in range(0, 3):
                if not self.isNotDuplicated(self.getSquare(3 * i + 1, 3 * j + 1, board)):
                    return False
        return True

    def getSquare(self, x: int, y: int, board: List[List[str]]) -> List[str]:
        result = []
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                result.append(board[j][i])

        return result

    def isNotDuplicated(self, nums: List[str]) -> bool:
        table = {}
        for num in nums:
            if num is ".":
                continue
            if num in table:
                return False
            else:
                table[num] = 1
        return True
