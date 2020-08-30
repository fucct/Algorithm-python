from typing import List


class SolutionJongman:
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [1, 0, -1, -1, -1, 0, 1, 1]
    board = [['N', 'N', 'N', 'N', 'N'], ['N', 'E', 'E', 'E', 'N'], ['N', 'E', 'Y', 'E', 'N'], ['N', 'E', 'E', 'E', 'N'],
             ['N', 'N', 'N', 'N', 'S']]

    def hasWord(self, y: int, x: int, word: str, board) -> bool:
        if not self.hasRange(y, x):
            return False
        if len(word) == 0:
            return True
        if board[x][y] is not word[0]:
            return False
        if len(word) == 0:
            return True

        for i in range(0, 8):
            if self.hasWord(y + self.dy[i], x + self.dx[i], word[1:]):
                return True

        return False

    def hasRange(self, y, x) -> bool:
        if y < 0 or x < 0 or x > 4 or y > 4:
            return False
        return True
