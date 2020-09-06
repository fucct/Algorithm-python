def solve(height, width, gameBoard):
    fx = -1
    fy = -1
    for y in range(0, height):
        for x in range(0, width):
            if gameBoard[y][x] == ".":
                fx = x
                fy = y
                break
        if fx != -1 and fy != -1:
            break
    if fy == -1 and fx == -1:
        return 1

    res = 0

    if fx + 1 < width and fy + 1 < height and gameBoard[fy + 1][fx] == "." and gameBoard[fy][fx + 1] == ".":
        gameBoard[fy][fx] = gameBoard[fy + 1][fx] = gameBoard[fy][fx + 1] = "#"
        res += solve(height, width, gameBoard)
        gameBoard[fy][fx] = gameBoard[fy + 1][fx] = gameBoard[fy][fx + 1] = "."

    if fx + 1 < width and fy + 1 < height and gameBoard[fy][fx + 1] == "." and gameBoard[fy + 1][fx + 1] == ".":
        gameBoard[fy][fx] = gameBoard[fy][fx + 1] = gameBoard[fy + 1][fx + 1] = "#"
        res += solve(height, width, gameBoard)
        gameBoard[fy][fx] = gameBoard[fy][fx + 1] = gameBoard[fy + 1][fx + 1] = "."

    if fx - 1 >= 0 and fy + 1 < height and gameBoard[fy + 1][fx] == "." and gameBoard[fy + 1][fx - 1] == ".":
        gameBoard[fy][fx] = gameBoard[fy + 1][fx] = gameBoard[fy + 1][fx - 1] = "#"
        res += solve(height, width, gameBoard)
        gameBoard[fy][fx] = gameBoard[fy + 1][fx] = gameBoard[fy + 1][fx - 1] = "."

    if fx + 1 < width and fy + 1 < height and gameBoard[fy + 1][fx] == "." and gameBoard[fy + 1][fx + 1] == ".":
        gameBoard[fy][fx] = gameBoard[fy + 1][fx] = gameBoard[fy + 1][fx + 1] = "#"
        res += solve(height, width, gameBoard)
        gameBoard[fy][fx] = gameBoard[fy + 1][fx] = gameBoard[fy + 1][fx + 1] = "."

    return res


count = int(input())
for c in range(0, count):
    h, w = map(int, input().split())
    board = []
    whiteCount = 0
    for i in range(0, h):
        line = input()
        board.append([ch for ch in line])
        whiteCount += line.count(".")
    if whiteCount % 3 != 0:
        print(0)
        continue
    print(solve(h, w, board))
