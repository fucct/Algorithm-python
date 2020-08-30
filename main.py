from jongman.boggle import SolutionJongman

sol = SolutionJongman()

n = input()
words = []
for i in range(0, int(n)):
    word = input()
    words.append(word)

boards = []
while True:
    n = input()
    if n == "0":
        break
    board = []
    for i in range(0, int(n)):
        line = input()
        board.append(list(char for char in line))
    boards.append(board)
    board = []
sol.hasWord()
